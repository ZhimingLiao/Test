--2018-12-15 广医五院  ANDY
begin tran andy
    declare @var int = 0, @VarRegId INT = 0
    set @var = (select max_id from hismz..sys_id_generator
    where definition = 'patient_id')

    set @VarRegId = (select max_id from booking_center..sys_id_generator
    where definition = 'reg_id')

    --1.更新pid到表sys_id_generator
    update hismz..sys_id_generator
    set max_id = max_id + (select(select count(*) from hismz..tPtient))
    where definition = 'patient_id'

    --2. 更新预约库的reg_id
    update booking_center..sys_id_generator
    set max_id = max_id + (select(select count(*) from hismz..tPtient))
    where definition = 'reg_id'

    --3.得到临时表 TODO 需要调整ContactRelationShipFlag的对应码
    select right('00000000'+cast((row_number() over(order by a.patientname)+@VarRegId) as varchar(8)), 8) RegId, right('0000000000'+cast((row_number() over(order by a.patientname)+@var) as varchar(12)), 10)+'00'  PID, b.code response_type, cast(rtrim(ltrim(a.patientname)) as varchar(30)) name, cast(a.sexflag as varchar(1)) sex, a.birthday birthday,
        (case when a.dq in ('本区','本市') then '440100' else null end) home_district,
        cast(rtrim(ltrim(a.identitycardno))as varchar(20)) social_code, c.code nation_code, d.code occupation_type, e.code marry_code,
        left(rtrim(ltrim(a.address)), 80) home_street, rtrim(ltrim(a.contactperson)) relation_name, rtrim(ltrim(a.ContactAddress)) Patient_remark,/*TODO a.ContactRelationShipFlag*/ '01' Relation,
        cast(rtrim(ltrim(a.contactphone))as varchar(12)) relation_tel, cast(rtrim(ltrim(a.phone)) as varchar(12)) mobile_tel, (case when ISNULL(identitycardno,'')<> '' then '00001' end) social_type
    into #temp
    from hismz..tPtient a
    inner join hismz..TempOldPatientResponce(nolock) b on a.PatientTypelistname = b.name
    left join hismz..dic_nation_code(nolock) c on a.gz = c.name
    left join hismz..dic_occupation_code(nolock) d on a.mz = d.name
    left join hismz..dic_marital_status(nolock) e on a.hy = e.name

    --4.插入到患者信息表mz_patient
    insert into hismz..mz_patient_copy([p_id],[name], [sex], [birthday], [home_district]
            ,[home_street],[relation_name], [relation_code], [relation_tel], [response_type],[occupation_type],
                     [max_times], [max_ledger_sn], [setup_date],[marry_code],
                      [nation_code], [mobile_tel], [social_code], [build_opera], [social_type])
    select PID, name, sex, birthday, home_district,
              home_street, relation_name, Relation ,relation_tel,response_type,occupation_type,
              '0','0',GETDATE(), marry_code,
              nation_code, mobile_tel, social_code, '0000', social_type
    from #temp

    --5.插入预约库表bk_patient
    insert into booking_center..bk_patient_copy([reg_id], [outpatient_id], [name], [sex], [birthday],
                        [telephone], [address], [id_card], [responce_type])
    select  RegId, PID, name, sex, birthday,
            mobile_tel, home_street, social_code, response_type
    from #temp

    if @@ERROR <> 0
        begin
            rollback tran andy
            select '执行出错!'
        end
    else
        begin
            commit tran andy
            select '执行成功!'
        end

    --6. 删除临时表
    drop table #temp

