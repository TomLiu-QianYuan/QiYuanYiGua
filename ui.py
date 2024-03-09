import datetime

import streamlit as st
import borax.calendars as bc
import functions

st.code('''
观物吟
一物从来有一身，一身还有一乾坤。
能知百物备与我，肯把三才别立根。
天向一中分造化，人与心上起经纶。
仙人亦有两般话，道不虚传只在人。
''')

time = st.date_input("日期")
time2 = st.time_input("时间").hour
print(time2, 'h')
# time = st.time_input("选择时间:",datetime)

mode_to_select = st.selectbox('起卦方式', ['时间起卦', '报数起卦'])
# print(mode_to_select)
if mode_to_select == '报数起卦':
    three_num = st.text_input(label='请输入三个整数')
    if len(three_num) == 3:
        c = int(three_num[2])
        if c > 6:
            c = c % 6
        if c == 6:
            c = 6
        three_num = [int(three_num[0]), int(three_num[1]), int(three_num[2])]
    elif len(three_num) > 3:
        st.warning("你暂时只能填写三个数字哦")
start = st.button(label="开始起卦")
if start:

    st.code(bc.LunarDate.from_solar_date(
        time.year,
        time.month,
        time.day,
    ).strftime('%G') + functions.di_zhi_list[(time2 + 1) // 2] + "时")
    # print(functions.di_zhi.values()[0])
    if mode_to_select == '时间起卦':
        time_ = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).strftime('%G')
        year_gz = functions.di_zhi[time_[1]]
        # yue_gz = functions.di_zhi[time_[4]]
        # ri_gz = functions.di_zhi[time_[7]]
        yue = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).month
        print(yue)
        ri = bc.LunarDate.from_solar_date(
            time.year,
            time.month,
            time.day,
        ).day
        print(ri)

        shi = (time2 + 1) // 2 + 1
        # print(year_gz, yue_gz, ri_gz)
        a = year_gz + yue + ri
        b = year_gz + yue + ri + shi
        c = b
        if c > 6:
            c = c % 6
        elif c == 6:
            c = 6
        print(a, b, c)
        three_num = [a, b, c]
    # 开始起卦
    result = list(functions.get_gua(three_num[0], three_num[1], three_num[2]))
    print(result[0])
    print(three_num, 'b')
    show = []

    for x in range(0, 2):

        zhu_gua = str(functions.gua_to_images[result[0][x]])
        hu_gua = str(functions.gua_to_images[result[1][x]])
        bian_gua = str(functions.gua_to_images[result[2][x]])
        print(zhu_gua, '\n')
        print(hu_gua, '\n')
        print(bian_gua)
        for m in range(0, 3):
            show.append(zhu_gua.split('\n')[m])
            show.append('\t\t')
            show.append(hu_gua.split('\n')[m])
            show.append('\t\t')
            show.append(bian_gua.split('\n')[m])
            print(x * 3 + m)
            if (x * 3 + m) == 6 - c:
                show.append('\tO')
            show.append('\n')
        print(show)
    st.code("".join(show))

