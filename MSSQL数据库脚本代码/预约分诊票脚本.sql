--2018-12-15 广医五院 ANDY
declare @ScheduleId varchar(8)= '',
		@QueueSn varchar(3) = ''

set @ScheduleId = rtrim(ltrim(:schedule_id))
set @QueueSn = rtrim(ltrim(:queue_sn))

--set @ScheduleId = '296130'
--set @QueueSn = '8'

--判断是数字
if not (@ScheduleId not like '%[^0-9]%')
  begin
     set @ScheduleId = '0'
  end

if not (@QueueSn not like '%[^0-9]%')
  begin
     set @QueueSn = '0'
  end

if not exists(select top 1 * from booking_center..bk_detail where schedule_id = @ScheduleId and queue_sn = @QueueSn)
	begin
	 select '数据有误!' PID, '广州医科大学附属第五医院' org_name,0 sequence_sn,'' ampm,'' patient_name,'' doctor_name,
			'' DeptName, '数据有误!' room_name, convert(varchar(20), GETDATE(),20) print_date, '' hinttimearea,'' reser_flag
	end
else
	begin
		SELECT
			bp.code_no PID,
			do.org_name,--单位名称
			bd.queue_sn sequence_sn,            --排队号
			bp.[name] patient_name,        --患者姓名
			s.shift_name ampm,
			dod.doctor_name,        --医生姓名
			dodp.dept_name DeptName,
			dodr.room_name,    --诊室名称
			convert(varchar(20), GETDATE(),20) prin0t_date,
			case bd.booking_type when 2 then '加号' else convert(char(5),bd.advice_time,14) end hinttimearea,
			case when bd.book_date is not null then  '(预约)' else '' end reser_flag
		from booking_center..bk_detail bd(NOLOCK)
		left join booking_center..bk_schedule bs(NOLOCK)  on  bs.schedule_id = bd.schedule_id
		left join booking_center..bk_patient bp(NOLOCK)  on  bp.reg_id = bd.reg_id
		left join booking_center..dic_organization_doctor dod(NOLOCK)   on  dod.organization = bs.organization    AND dod.doctor_code = bs.doctor_code
		left join booking_center..dic_organization_dept_room dodr(NOLOCK)   on     bs.room_sn = dodr.room_no
		left join booking_center..dic_organization do(nolock) on  dodr.organization = do.organization
		left join booking_center..dic_shift s(nolock) on bs.shift=s.shift_code
		left join booking_center..dic_organization_dept(nolock) dodp on dodp.dept_code = dodr.dept_code
		where bd.schedule_id = @ScheduleId
		and bd.queue_sn = @QueueSn
	end
