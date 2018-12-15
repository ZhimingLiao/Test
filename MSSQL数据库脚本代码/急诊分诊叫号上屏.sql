if OBJECT_ID (N'tempdb.dbo.#temp_list') IS NOT NULL
	DROP TABLE #temp_list
if OBJECT_ID (N'tempdb.dbo.#wait_list ', N'U') IS NOT NULL
	DROP TABLE #wait_list
if OBJECT_ID (N'tempData1', N'U') IS NOT NULL
	DROP TABLE tempData1
if OBJECT_ID (N'tempData2', N'U') IS NOT NULL
	DROP TABLE tempData2
if OBJECT_ID (N'tempData3', N'U') IS NOT NULL
	DROP TABLE tempData3
if OBJECT_ID (N'tempData4', N'U') IS NOT NULL
	DROP TABLE tempData4
if OBJECT_ID (N'tempData5', N'U') IS NOT NULL
	DROP TABLE tempData5
if OBJECT_ID (N'tempData6', N'U') IS NOT NULL
	DROP TABLE tempData6

declare @doc1 varchar(10),@doc2 varchar(10),@doc3 varchar(10),@doc4 varchar(10),@doc5 varchar(10),@doc6 varchar(10),
		@timeout varchar(100), @Notify varchar(100)

if CONVERT(varchar(100), GETDATE(), 24) > '20:50:00' or CONVERT(varchar(100), GETDATE(), 24) between '13:10:00' and '14:10:00'
	begin
		select '今天已过看诊时间' Result
		return
	end

if CONVERT(varchar(100), GETDATE(), 24) < '07:30:00'
	begin
		select '看诊时间尚未开始' Result
		return
	end

select b.doctor_name, a.p_id, p_name, a.schedule_id, a.notify_count, a.notify_date,
	a.notify_status, a.queue_sn,a.dept_sn, a.invalid_time, a.[status], c.room_name,
	a.room_sn, '     ' flag
into #temp_list
from booking_center..bk_waiting_visit a
join booking_center..dic_organization_doctor b on a.doctor_code = b.doctor_code
left join booking_center..dic_organization_dept_room c on a.dept_sn = c.dept_code and a.room_sn = c.room_no
WHERE  convert(char(10), a.invalid_time, 120)between CONVERT(CHAR(10), GETDATE()-1, 120)
      and CONVERT(CHAR(10), GETDATE() + 1, 120)
      and a.[status]IN ('3', '10', '11','13')
      and a.room_sn in (206,207,208,209,210,490)
order by a.schedule_date desc

--患者隐私处理
update #temp_list
set p_name=stuff(p_name,2,1,'*')
--下一位
--3已分诊 10已通知  11正在就诊,13 回诊
UPDATE a SET  a.flag='next'
FROM #temp_list a
WHERE  a.[status] IN('3','10')

--就诊中
UPDATE a SET  a.flag='visit'
FROM #temp_list a
WHERE  a.[status]='11'
AND NOT EXISTS(
	SELECT TOP 1 1 FROM #temp_list b
	WHERE a.schedule_id=b.schedule_id
		   AND a.queue_sn>b.queue_sn
	       AND b.[status]='11'
)

--过时
UPDATE a SET  a.flag='out'
FROM #temp_list a
WHERE  a.[status]='10'
--AND notify_date is not null
and DATEDIFF(MINUTE, (case when notify_date IS null then invalid_time else notify_date end), GETDATE()) > 30

--select room_name, p_name, * from #temp_list
set   @timeout = (select STUFF((select
            + '、'+ p_name
            FROM #temp_list
			where flag = 'out'
            FOR XML PATH('')
            ), 1, 1, ''))

select [1号诊室]  "1号诊室", [2号诊室]  "2号诊室", [3号诊室] "3号诊室", [4号诊室]  "4号诊室", [5号诊室] "5号诊室",[抢救室] "抢救室"
into #wait_list
from (select room_name,(convert(varchar(3), queue_sn)+' '+p_name) p_name,queue_sn from #temp_list where flag = 'next') A
pivot(max(p_name) for room_name in ("1号诊室", "2号诊室", "3号诊室", "4号诊室", "5号诊室", "抢救室")) b
group by queue_sn,b.[1号诊室],b.[2号诊室], b.[3号诊室], b.[4号诊室], b.[5号诊室], b.[抢救室]
order by queue_sn asc

declare @i int = 1
DECLARE @sql VARCHAR(MAX)=''

while @i<7
	begin
	set @sql=''+
 'CREATE TABLE tempData'+CONVERT(VARCHAR,@i)+'
 (
	id int identity(1,1),
	name varchar(20)
 )'
	set @i = @i+1
	exec(@sql)
end


insert into tempData1(name)
select [1号诊室]
from #wait_list
where [1号诊室] is not null
--order by [1号诊室] desc

insert into tempData2(name)
select [2号诊室]
from #wait_list
where [2号诊室] is not null
--order by [2号诊室] desc

insert into tempData3(name)
select [3号诊室]
from #wait_list
where [3号诊室] is not null
--order by [3号诊室] desc

insert into tempData4(name)
select [4号诊室]
from #wait_list
where [4号诊室] is not null
--order by [4号诊室] desc

insert into tempData5(name)
select [5号诊室]
from #wait_list
where [5号诊室] is not null
--order by [5号诊室] desc

insert into tempData6(name)
select [抢救室]
from #wait_list
where [抢救室] is not null
--order by [抢救室] desc



if exists(select * from #temp_list where /*DATEDIFF(MINUTE,  notify_date, GETDATE())>5
	and */ notify_status = 2 and [status] =10)
	begin
		set @Notify =(select top 1 '请 ['+ convert(varchar(2), a.queue_sn) +'] 号 ['+a.p_name+'] 前往 ['+a.room_name+'] 就诊'
		from #temp_list a
		where /*DATEDIFF(MINUTE,  notify_date, GETDATE())> 5
			and */notify_status = 2 and a.[status] =10
			and a.flag != 'out' --增加对过号患者进行过滤  2018-12-12 广医五院 ANDY
			order by notify_date desc
			)
	end

--select * from #temp_list
set @doc1= (select top 1 doctor_name from #temp_list where room_name = '1号诊室')
set @doc2= (select top 1 doctor_name from #temp_list where room_name = '2号诊室')
set @doc3= (select top 1 doctor_name from #temp_list where room_name = '3号诊室')
set @doc4= (select top 1 doctor_name from #temp_list where room_name = '4号诊室')
set @doc5= (select top 1 doctor_name from #temp_list where room_name = '5号诊室')
set @doc6= (select top 1 doctor_name from #temp_list where room_name = '抢救室')

-- 增加对数据是否为空判断,如果为空,其它和数据无关,如时间,仍需要输出
if exists(select top 1 * from  tempData1 a
full join tempData2  b on a.id = b.id
full join tempData3  c on (case when isnull(b.id,'')='' then a.id  else b.id end)=c.id --a.id = c.id
full join tempData4  d on(case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id else a.id end) = d.id
full join tempData5  e on (case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id  when ISNULL(d.id, '')<> '' then d.id else a.id end) = e.id
full join tempData6  f on (case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id  when ISNULL(d.id, '')<> '' then d.id  when ISNULL(e.id, '')<> '' then e.id else a.id end) = f.id
)
	select a.name [1号诊室], b.name [2号诊室], c.name [3号诊室], d.name [4号诊室], e.name [5号诊室], f.name [抢救室],
	CONVERT(varchar(100), GETDATE(), 23) NowDate,  CONVERT(varchar(100), GETDATE(), 24) NowTime,@timeout [TimeOut],isnull(@Notify,'') Notify,
		@doc1 Doc1, @doc2 Doc2, @doc3 Doc3, @doc4 Doc4, @doc5 Doc5, @doc6 Doc6,
					(case when datename(weekday, getdate())='星期一' then '周一'
					when datename(weekday, getdate())='星期二' then '周二'
					when datename(weekday, getdate())='星期三' then '周三'
					when datename(weekday, getdate())='星期四' then '周四'
					when datename(weekday, getdate())='星期五' then '周五'
					when datename(weekday, getdate())='星期六' then '周六'
					when datename(weekday, getdate())='星期日' then '周日'
					end) NowWeek
	from tempData1 a
	full join tempData2  b on a.id = b.id
	full join tempData3  c on (case when isnull(b.id,'')='' then a.id  else b.id end)=c.id --a.id = c.id
	full join tempData4  d on(case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id else a.id end) = d.id
	full join tempData5  e on (case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id  when ISNULL(d.id, '')<> '' then d.id else a.id end) = e.id
	full join tempData6  f on (case when isnull(b.id,'')<>'' then b.id  when ISNULL(c.id, '')<> '' then c.id  when ISNULL(d.id, '')<> '' then d.id  when ISNULL(e.id, '')<> '' then e.id else a.id end) = f.id
else
	select '' [1号诊室], '' [2号诊室], '' [3号诊室], '' [4号诊室], '' [5号诊室], '' [抢救室],
	CONVERT(varchar(100), GETDATE(), 23) NowDate,  CONVERT(varchar(100), GETDATE(), 24) NowTime,@timeout [TimeOut],isnull(@Notify,'') Notify,
		@doc1 Doc1, @doc2 Doc2, @doc3 Doc3, @doc4 Doc4, @doc5 Doc5, @doc6 Doc6,
					(case when datename(weekday, getdate())='星期一' then '周一'
					when datename(weekday, getdate())='星期二' then '周二'
					when datename(weekday, getdate())='星期三' then '周三'
					when datename(weekday, getdate())='星期四' then '周四'
					when datename(weekday, getdate())='星期五' then '周五'
					when datename(weekday, getdate())='星期六' then '周六'
					when datename(weekday, getdate())='星期日' then '周日'
					end) NowWeek


-- declare @i int = 1
-- DECLARE @sql VARCHAR(MAX)=''
set @i = 1
while @i<7
	begin
		set
	@sql=''+
	'drop TABLE tempData'+CONVERT(VARCHAR,@i)+''
	set @i = @i+1
	exec(@sql)
end
