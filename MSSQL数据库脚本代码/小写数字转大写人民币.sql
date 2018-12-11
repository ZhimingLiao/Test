USE [hismz]
GO
/****** Object:  UserDefinedFunction [dbo].[toUppercaseRMB]    Script Date: 12/10/2018 18:04:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
--2018-12-10 广医五院 志明
ALTER function [dbo].[toUppercaseRMB] ( @LowerMoney decimal(18,4))
returns varchar(200)
as
begin
   declare @lowerStr varchar(200)
   declare @UpperStr varchar(200)
   declare @UpperPart varchar(200)     --长度
   declare @i int

   set @lowerStr=isnull(ltrim(rtrim(convert(decimal(18,2),round(@LowerMoney,2)))),0)
   set @i=1
   set @UpperStr=''


   while(@i<=len(@lowerStr))
   begin
        select @UpperPart=
        case substring(@lowerStr,len(@lowerStr)-@i+1,1)--取最后一位数
            when  '.' then '圆'
            when  '0' then '零'
            when  '1' then '壹'
            when  '2' then '贰'
            when  '3' then '叁'
            when  '4' then '肆'
            when  '5' then '伍'
            when  '6' then '陆'
            when  '7' then '柒'
            when  '8' then '捌'
            when  '9' then '玖'
        end
        +
        case @i
            when 1 then  '分'
            when 2 then  '角'
            when 3 then  ''
            when 4 then  ''
            when 5 then  '拾'
            when 6 then  '佰'
            when 7 then  '仟'
            when 8 then  '万'
            when 9 then  '拾'
            when 10 then '佰'
            when 11 then '仟'
            when 12 then '亿'
            when 13 then '拾'
            when 14 then '佰'
            when 15 then '仟'
            when 16 then '万'
            else ''
        end
        set @UpperStr=@UpperPart+@UpperStr
        set @i=@i+1
    end
    set @UpperStr = REPLACE(@UpperStr,'零拾','零')
    set @UpperStr = REPLACE(@UpperStr,'零佰','零')
    set @UpperStr = REPLACE(@UpperStr,'零仟零佰零拾','零')
    set @UpperStr  = REPLACE(@UpperStr,'零仟','零')
    set @UpperStr = REPLACE(@UpperStr,'零零零','零')
    set @UpperStr = REPLACE(@UpperStr,'零零','零')
    set @UpperStr = REPLACE(@UpperStr,'零角零分','')
    set @UpperStr = REPLACE(@UpperStr,'零分','')
    set @UpperStr = REPLACE(@UpperStr,'零角','零')
    set @UpperStr = REPLACE(@UpperStr,'零亿零万零元','亿元')
    set @UpperStr = REPLACE(@UpperStr,'亿零万零元','亿元')
    set @UpperStr = REPLACE(@UpperStr,'零亿零万','亿')
    set @UpperStr = REPLACE(@UpperStr,'零万零元','万元')
    set @UpperStr = REPLACE(@UpperStr,'万零元','万元')
    set @UpperStr = REPLACE(@UpperStr,'零亿','亿')
    set @UpperStr = REPLACE(@UpperStr,'零万','万')
    set @UpperStr = REPLACE(@UpperStr,'零元','元')
    set @UpperStr = REPLACE(@UpperStr,'零零','零')
    if left(@UpperStr,1)='元'
        set @UpperStr = REPLACE(@UpperStr,'元','零元')

	if @UpperStr = '零圆'
		begin
			set @UpperStr = '零'
		end
	else
		begin
			set @UpperStr = @UpperStr
		end

	return @UpperStr
end


