import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout='wide', initial_sidebar_state='collapsed',page_title='고1 수학 공식',page_icon='➕')

menu = st.sidebar.selectbox('단원',['1단원.다항식','2단원.방정식과 부등식','3단원.도형의 방정식','4단원.집합과 명제','5단원.함수','6단원.경우의 수'])

st.write('이미지가 안뜬다면 메뉴를 다른 곳으로 바꿨다가 다시 돌아와 보세요(새로고침X)')

data = [
    {
        'category':'1단원.다항식',
        'url':'https://blogger.googleusercontent.com/img/a/AVvXsEiSG3F-8jQgh4Jyma9uQxHiPSOrK4asMzCRMtioQ5-npPMYRs3pG30xu-q6ys9QbwXMF_Vj0XwpMKr25VtOQ3bPvn5IvTOZEtmUcReHsjnwq_VFKtEWn_mmjIhMUDg3d5Htl5eJleQJS5pEyyyY4tps5PZHTnI2M9R0XjZG2nMhkFgFzlVdMCC7jT2HSw',
        "name":'곱셈공식'
    },
    {
        'category': '1단원.다항식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhVg5BROfDiHGXIt8gjRmjbMwoVlwfNkMPRbJFVOCCFY17yiDQrbPfwQOPEvVLC4voZ4bvyJKbZ27soVTfPJr07jzQO8quHw7HBynhKHKYa-OG2F4RVLwS-OTPZ8Plwzqi7U5BfkPO9n8bgCNKOq0BDFJwRt2oKEe7KfakdkgGI_uIbU1LF6J54GZX6Ng',
        "name": '인수분해공식'
    },
    {
        'category': '1단원.다항식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhawOleRrTaNPCeqDPdEtpzFzG5C_Khm4Xzt6yegpEjPrcmW41fUifYPSHqYG90T1JcPfiNUOom6fPKMW07R27eGfoN8iI5Ua8GGxKF3EIiagPsDsml9B-O5yKU-BNCUMoTnDepEghYz8p56XqpAbevTB18ANfQQ3kC-pxSAN1PzclTgdc1oLevOJja9g',
        "name": '미정계수법'
    },
    {
        'category': '1단원.다항식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjIjrMy55h8i5lVrlzt0sapCSmJbgolMSD4pJtaSRovF_xFTHEoy8vugJH9aBqKNZJxuy1PWSHcmFhQUWYBkvtICcnPXk46rZPnKCOMjzug3J7gU-qQpLdA-LVaDnz9b3aLF3yq1fiidnmzTKdBCvGdwaOntvX8bb9jrWYcad3ZA1nAO4SvT0LSjiYBBg',
        "name": '나머지정리'
    },
    {
        'category': '1단원.다항식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiPBSqIEW_rxbu5uS7dBcRa_TpToP76pu9LuedKVQqqULxMMtYzAtOWxn_hyHvjUNitDv3c3XrvTAxuDWwzx8QNrgFY1R65ysdXcxfTDXx2Ov8SwnMZMDS0jm09DE3DHAcNTd1wN2QaZKMuAsMFDV6uHLimu4KlgENntTlHb2hrt83yYYBThjiwfpOMTg',
        "name": '인수정리'
    },
    {
        'category': '1단원.다항식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhrw5ss1RbnLzxOuX9HdhvTHkq2nYRytn0Usidz6VlrxA9xO_4aR2I4BTFIt5cAGv_ZBbMkrr7ddI4osmthUSjb_NuMHek2LOv8SZ8YG80cpegP-Jo-E6rxzUmqrVGCJdT7WdQqAPDr91uJkrVRdBK9E_Fe1nTvFT0pL-7v7vSO8psiH3z9YOyedVUAuQ',
        "name": '약수'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhZUqZ_72bpUtYtVMCCOPfcf4J8RJ2LL-l_L4Jd1zEDBSVdiygfea6_fVERRa2yKAtE-XvIAKBqHiXoCKLuL9Hg9d4nk5kJGKFl1m0NSjnB_KcxhkCmiwMRN7KW8ayUEILaBjncMqKwzh4ORRhZEMFUEPZesuPKb4w4pKzsY7gjBliTstA_7477Nx0Z8w',
        "name": '복소수의 덧셈과 뺄셈'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEi3zLTeemxFQ3DdD-PPvbC9DVcPrl0KFfzvpTkrwcy1He-FbyahucbYTcyI6RxmJ2dGTcdES9CIntPIIqEMwhCHMZGqF_2dAs0MrXDQ4SBL2ZIL7DwGuOemfcDzc_0Ur8TDzmTSBYwvy696JkUt9HByHjhZcOjlw0BOnk6xSK-3l4c6S7G3Ntxstsx3Ag',
        "name": '복소수의 상등'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEj6i-T3o_XTCnU-8BANKLYpzNiK2wJcCg8uA1wLjpXn5tUhkkJkX13OyBYMDaMWYgHFOhAJjexbPJ4amPsxPLUdaleDhagR0H-ziJK0-kllBJkywk7rK7M8Uwzke_7fLHF81lvVjgTttoPHmWmoJSulpgbMXTNei-HulYUSR_D12CL2UEulizKjPpLmGQ',
        "name": '복소수 분모의 실수화'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiNHho3u40m4ovFLUtN29Qos0ZHNOXfMNzHBeOsADAqaRhuwkl0E4uAYjq2Cd6Wx9-DThMEy-uBJ9tF9tpv8F3ryUEjZnkppSshJEHc8kvqE1Jh53hJySxoh85zhHuDzCnbw6VDJa2wryDHjU5qdTo7ILdfCTjDo-Fp8AOXna9CJvoCL2zyEJSQpENFlg',
        "name": '허수i의 거듭제곱'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEg9LZxnZK4ncvGgtmj7ACPYN0nGWaGp-BNUVkt3wUn0juYymLfs3388yXPNi0dsb63QKF4F8B26ytgmfTVoPGrgfBLnKgnESZJt42rtJyKx4Lack4aDQZDELGRXDukFMvmkA-pRRXlRqCpxxLlk4MDB0x6_ZzLYxF_0PQZ8Am58lb3vLtA8k8qr0LZySA',
        "name": '자주 이용되는 i의 거듭제곱✨'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgWP4KiCcdtAhv2l3JdrTq_9B7luRwZVu7hzft7T1LqAqjZMuPewK7g68HUuURwbZ5k5SPLtd7-F5Fgx9Pt_ZCE7Z02iqJ4YxmwUhYd1Gipg2w9l-pSogCxPmMIkXwYACqE5brHkMTEXXYjJsL6hWs_mxshFMxWXQ82_H8P32U8xwmZDSxTBjLPRgdq6w',
        "name": '켤레복소수'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiiS6WZLb6zGuxNaF21vgD7iTz35Bym48ark87usBoWlmYtWmXNSEmDG4LUDLnpcGDRcGphhRooXUwQLhRyswuizPpgun_J7-rxynrVA76ZcYEio68BslgO7BSi2GVuIB_54R7KGx6vPwH7fJNd4M95pxtx4QHlY3VufZsnY-SNdVfjis6yhpZhwk-9LQ',
        "name": '오메가'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgiWaBGNfaA7pFpw7u3iOgDSGMBJaAMQkdj_0CtImFpmeeRrHJV_iwxcF6-SYSGn42MASXHnMTiRahujETDVOks0Jg1fBr1bcPVt_ldtoZH5DT-Ip469pOCY4QAsaxbjAwAbMR3oqbmV3q7pHPozKOw9NZEVkllYxazaOWr8T3V29ZcWcnXlv3LfJpbZA',
        "name": '음의 제곱근의 성질(화질 구져서 죄송해용)'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiroVE1L_eE60EUqHEhnNZNezG-PolnsqXD6ks-DSzO1DmxvGpMFf1moCzIl7jm39-G-dQqGhK00mD-WesGJjJcCxt81sk-HvHniyVGVz42dEKXFDdmmxExj0oH1NyS8tPN8oWNeztno0yNZSrigkEjFcGRPDvuh_YVkmUfLfzxKJtwFuSlmCB-HMDtMA',
        "name": '이차방정식 공략(1)'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiDL5qKGlRRpYW2R0K5wU8fXO1iA_92-L_AqNd0-THeh0bF1QhKISM-LDRwjhnJjQq0JjA_rA6k50fG7XqKkUmkwUCbga8X-5xjSCcIt6MwCWzfSpM61qd0UsmFrXLqw3N6OHsmKVwevZpxSldv7Py_ZhMmDN--XbjsAcoghHNITIOuEt-Sej2N4t8JeQ',
        "name": '이차방정식 공략(2)'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhkYCI8vlyq2eED6QIgZF0oFcPaSWpoGur1rilvvoiTF4prjDHVLuBoMYNdFzPqCmfOa5Pc2C037otZY82qkL8B0Ob3I5tbQ-N3mTEBIufGuv6AX0kC4xk2wh3rI2MwHTUm8icUfBbcWQsCrqrw1kq7fWPUjeb_Ngo7pA9e0rXOYwVGlP6qFEWziDICVA',
        "name": '판별식D'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEj9uW1EbzCf1lTdNMvYlUP0TA7mXLjx_LQFjNiYfvUeL_R3zr-sTCWHoEFxckNpm6LGDaZPTMdCQNSAOhy1uBCVgt1LPqJ9hR91Yjbty7Mub7vv_QNKht91E6pUwR-ttOlALd-BBp7gxTGNd811JiLaipLX24TPOISf2pzurxhjWe1saJY9X5xMH-82CQ',
        "name": '판별식D의 활용'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgSlmuuiK-LaqJVfzTZIuoSuMNux4KNoNm-xXpaF1LQgDunPr8ebRIiuKc3vE2bTkczEro8rLAlCxRfHIBbzYR0Ep2_IhVanbnav5bF7tsh3FhyC9y13PlX8xll6GJjesKsV7NXQCt4qKyBQgoSutjoaQMFK6gHjsXVFpvS77ogmo-XgsxInqm_tuWBTQ',
        "name": '근과 계수의 관계'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhhWNSDcU4sBlzO1oQnQqJqFBtEZxo--ert1brRP3iSZ5AdZcWsgH4eSgRprWp0AZtL5Lg6YQyGP0EXvrNuk0hYxxzx5GWKt49RVB9rrWQLm-CIUav7OuJfv5XfB12Q9WkbldXGZoQ4vZ4numDAkozcmx1GWRwxU9KF9WRu-xyj_8OsLPLVf1AL234VVw',
        "name": '근의 부호 구하기'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEidre1B-TVpF3IB85Y2A1sLSHFctyVA9wIxXuPeXSMdsG7drbl-bnfs8tC0Ik9bipOeMH_AAajREAHySjZ_oQgqJ4bOQnc-CVrFmaOzJ3IH_H1UmNH8en-1VFb2QTsxMyyQRbqLyE73S1xGK1StKTZkENkNzR3U-M7Pnpzq6-Jnh-4ctPFJ-mcoiSSrhw',
        "name": '이차함수 그래프의 성질'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEicZoxIOeu7Tsn9hUSZO-4g3DJSJ5qAGd0bPEz8ejEbDrPYxoFgitB-_IEJ3T_LLQgMYEzLgK5nBW4A7WDDfMMBQm5v-Ic-2W_fvALGWPQxZoB7f04aMWUWLBoIFNBc2LbpkJzm_JzBWwjkZcU0qCXrrt0prSaWvKi3e5XRnA0bCggjtrcyFWDa6W4wtw',
        "name": '절댓값 기호를 포함한 식의 그래프(1)'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhP0MKWzbEYSU8upMjGQpxKZriPFOI6Ltp-nI89PARb-bJq7evr2ACJmKotBwVJztNrZjytx6lLq5P2dExJpKj6AWtEgWwUhugSMjyhsplzx8TPj_aRNyPQGtoWluNbXzLQxvLaPvz2itL_ctSvdLGkGJufQ1DUMEoBS4TLq3N7_FL-mo8BGMvCWQjdug',
        "name": '절댓값 기호를 포함한 식의 그래프(2)'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgEo07asVnL4Yy1I3GmpAJCZBYVQ3pxKGzkaA3UdOQIsDqLTKlt5_G6rtTH0OH4MuWrS4XJLMGpsu2o8TIZZ9YY5qR0DXxjiwduXW8_6y1Y7LVN1szbhu8EMX_9ndKy0u6qzPTOSBlUI5Ji3tM-bm94JFjWgbqSP_LjdwOHQltKOMYizHNQRjA_Eh9Pvg',
        "name": '이차함수 그래프와 직선의 위치관계'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEg63coF_9Sg3uk_4laXQ3_UvLot9c0TURHuVcKKOdllzc8_Z1iP-xayo3BDb0RFhabvKYrYiX1v5ngU-nT5ELlPlNyvRnYlv0r3n3zxR6Kvac3QiC4t1dZ2-bCyI7QP5LVt18UAx4bsTdPWpBfp-rDwntJgNP31Gb4B-4sxpS8vyCaATL0JFaMsy736sA',
        "name": '일차부등식'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjmkgJmrjBPIQ8zeWbwum4HO0AcLi30xKU9M9E_xi7fN9L4xGIGYya-_zv33mtEAOs09dbpPwzPQ3ca-5cPtL97aclKC8xM23aQB-L8t-I_ZXxfTRydKA6rWkzoCnKeH09ALd5kX7AdSivF_oSpq9JHIsX3pvrfPXdTEbztDuD-ZxBJRFgw5CkvI7FXTA',
        "name": '일차부등식 그래프'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhIhxysmbbyhxVP6w-k_G35h5eTQtKRAdJqsyuaUsdDxecgoS3-Vb28b5Yx0sf5mFnNdt9Nsj4exfG3F-WQWX_rLYmDbkQPrk6YjdIY6CN8ds0q8m8ckrjLrkNn7r8Ykutf87Z5AJiKEoNslYdlN8qD_sN-t2xtbElar6KpkHZbONiLjcN3iYUEwbC8iQ',
        "name": '튻후한 해를 가지는 연립부등식'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEg_y56W9rS5qE7GkUfYYKwUD9sa-Q_YGY9DvYyjIPvh9NKV3m6PmD9v4gfAfvjMhAZMxeo4fHvrHUfrsZEWuZ8tmaZaU1UUZIT4H6bKkEQHYPs-p3QZUMNVvlhYxqqMxyope43mso5hKMMFpElRWsnfsxgomzhWNmw6mgQAdazIQmi7qMYrbQk5Dm22eQ',
        "name": '이차부등식'
    },
    {
        'category': '2단원.방정식과 부등식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgU9dLFHXbA5iST7A-FJwaDA5x51u212QCnaMllR3kOKGPGhMqBMYckHBxWB2BZztWIFxaXyMKDHx4lds4enN9yaghlMnssmIGgL0FiKbXmPpzDQxJBZoH5JHrq4F3irinmTQNNvFkIP1ec-pvnIOLSlKhKCV24cXHqCDV26_xGAtOBpUErWcFfcLQ9DA',
        "name": '이차부등식이 항상 성립할 조건'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjyUQmNbrqlaDvxMQRpk3-UGM0YG-3m0jHd-cDFPxQWW5G2EqGFm42CaeO7HZjJqXNdY9muXcA6a-20-FjGQ1CjVafloNOnFirFRap30mmO8vmIvov0VFslYh13S0KXdSFQ30PVH2CireBrRJ8uoPyx3EWGXTNT7IebMUE0czy5PxKgJiUcHHA8HiCthQ',
        "name": '수직선 위와 좌표평면 위의 두점 사이 거리'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhNrbGjG_0NjT09O8N28FDu7i__oRkrRde-XDPibaC4Ac9Ah4Ys_zs-bvKnmiiQ2QDQAtNLUMTZQg3d-oVgWa5dkSXY5yG53e0w9br_HwTg0pc8RjSKVn6gU1qYv0pvwqGvjtWL8GpA0Qhmp3-pzscfMaI6XOWu945_4N23nYSSiOuPQ37LP4qPAYDJtw',
        "name": '선분의 내분점과 외분점의 좌표'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhYxPgArCRs8OQ91_Z65-kd0wFRGj94XutwNTFuM4TIrEhchYbP8VCzENQ2Yk0Lsxr-gE3R6k-6Y-CJiiL28ewYznMz3wRUwMa5JX1tdddd0NcEkPer9cEZk2TumjxrdPF0rtidlQehjATFZKRaIcxwZAwDQaZQM9z-1PEBqXDDgQkfk458J1WnkKaC_w',
        "name": '삼각형의 무게중심 구하기'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEg3d9qqOx-GWse-1hURTiQXmTJEbQdaMEE0Fq1EVdycbNWsSs0VWdXFp2q5ZBWTTNcEQaNLay9n80xcsuwyMAZyGVQ-9fVFD2O5kSnWR5zHC1qAMR6jhhpqWjkAgsFR29UlDuqzHAEJvJSgs7VV9pb1XeyYR_mOovu4TfqU92rt_C4cASvTgRXcst3Vgw',
        "name": '중선정리'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgQOPfAg5JQwGYEC8qVUCYPDQBWF_jywB04Ge9R_nWTrnv0wsOnqypsAQJUVJeRPX-n_BM1JmswKwj3mfAD5k_BfrhxymokN-HR-WNweZjWQFWqfZ0QPRrVVS1jwzd-7usUndkIhUAu_N-2a-7atKofIZ8JWQoaqs22PGsi8-TP7aB_nxLTKt0cuFQ8zQ',
        "name": '직선의 방정식'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhvgsteqMemZQSwxUhlHz97OV79OgTRpKBaBuqJf3f9NXsztYtEuBsLIpgKlgETpjZkWgafje6aAkHMr_tM3JGzwDz9SDEgpyAJqZsME_K_iyiLxtQ4o47k0EC59-7GIbcNtBVgG01KK9pewWmzVU2_QUZ7_KIFMXNtpG4DMA01azeV3ok5W6hrp2zb3g',
        "name": '두 직선의 위치관계'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhq5_CIiH1_gbxuRh5-S8whEwWvmstxIDsxLvc0Z4Gr38Ha58X-UR0HQgxTFs1BadE9C2Ku8TrOfalE-LpCaYfqmLpc3YwTOdeInaPJQM5Qb_pWMS5RcZgMje4iPldCTtHcrAvkMmUe1U603z2-MHaKat65nZEk3922RMnpHYd0MrsRzbSyDeJgnNQnWg',
        "name": '제목'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgHnzn5wYcCaUghxz7YWWJ_Qac5BocEoxHtW-Dl9cdcMaA4Od06JycXdQafzSC2Ptjb_WUqiTlq1MlgkiXTFqgZxTqVKosIPvkfRmfHfpw-jpGuCMH9qI9lacsM2JWqh48FWifkSKZHeflAJxUopdMe4adm6pZfJT07-84hdfZ6Dv-XIRlHHhWTwNJnXA',
        "name": '평행한 두 직선 사이의 거리'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEiOauVd9UTZXew09foK2JGbfqrqy6AJpkWkzhZRUoecmkTZnVupJNvNT38YqW0gpXHva9PCZE0kz-2jqFSMdXehwlfvBT16E66y_VCe5H6u4qXL3HW668QaE73-Z9eUtQ2lCq6owbf1P3e75XyvAVVVTkr1uh95hoZd8LqUTFBDOp9PbzOhPSMMOG-U0A',
        "name": '원의 방정식'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjXkt76wtKZUy3VkbgYP9f_GISSSsBxMk3JeZav84MRFB9q3XW-Cvkx9ebYnzxrMThiFVP_uZI0s_AMYxZSozk43FdQZbcOPfO4CS9xztCY4OkBCgyYOiAV2O2Ul_KibdM9to6DJe3yNqwOr40TV_7HMOkZWsTPeyl5EOjboWNEHQyg9tckJeZFvATmlA',
        "name": '여러가지 원의 방정식'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEhrBcsJhM2efDOfVS2jkksEHZee9y-HGZk6c3j0Qg5u7pd6yxwC_MA8Aghz5kjjuArfcV7PujuBnNKHjrMwRqHe8wsGbgctlSHrl46kcaPLm0TeDoZa8oPjmrRHkdZuW51mNW5y7PbSuWYF-Tv9VvmvQe-1_Wc2TM5BtMEqPyD-TEHHiBnm_MCJX0HaBg',
        "name": '아폴로니오스의 원의 정리'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjwHjS77B54dAVOfAihB-RyiTOfME9Owfbv3wiksd34ZLflpVOyzBHRMpgrR8XggGR0PhFRxfY8Dqtxwlx_MNUv8v4Bh8871NJEa3UZWWy82SHHT9aZ3Gj1IfuzOpnA_9R4pSEhjeAbcweM4Se6xe5qaN0P5jG3eyT6Zpb3uXO4MIhKeRuHDpTfRG3PlA',
        "name": '공통현의 방정식'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgGjDXIS1f3onSc4URFznQBXI_nsNtdw-KT5ynSZXikH-CFoM1uzuzzFgRipgZHIvLbH5EsJu8X8ppYgHrFYc7frwRLMnFi1RdIj87Purpxtff6oPmPpUpyYOH7O_FSwFrYK_j7Mlfi2aPWARi0-Q2ux2pZcGRxaTRstMjq18UPcPmEeUawh-9TTpyVkA',
        "name": '공통현의 기울기 쉽게 구하기'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgRWS71m3BJzmuEuf9IajbuDcU3ZyEigTQwsSdvgh7gSPKmZzTbEsOJNEVjELaZ9R1blRQp68WC3gD_gWYhuzu88ITEwS4YnKVPwN-siSokF3m73pywkWY4AJl6QSSi6xzQZKfqAAlj_DABufYC9-8jMJ6qmIQ-H5IqvbuC8VLVil15mCSCEKSRwL27Lw',
        "name": '기울기가 주어진 원의 접선의 방정식 구하기'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEgfpsc8ALtJdwC66DtVCVDEhPaCuwSpzDXWRiyLLADXSwQcS01lkg5nVdwJWsbz3_JWLHsRmdpLZMkwLgYd2mHi8Q_Ko0e8N8Hmy1C31QpyG1UgUEmxl4puE50SxvWlJjwS9uw-6dhmvbpBm-D7Vtvkjp4uiqfHP-bNAduBRthT8bigSUS8wyG0atNFHA',
        "name": '원의 중심에서 직선 사이의 거리를 이용한 원과 직선의 관계'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEh-T6zRY_jRzPYyhY-wcsTw4cukq3Ka3vPL-XUlu6RMEu8ORhdN2X8Pg5cIhoYDpipyiIAo8CLj7qhitKuFbwb0rKleFq4dWtYcKHqKhvVz9jBIopEsuYYV7nGm3r0ToheF9CGoOxMl4ZCC5Lm0ClmxbsBo7ul3Ldkdsdly0zAIuWf_zyuYyPeURdBxwQ',
        "name": '판별식을 이용한 원과 직선의 위치 관계'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjbE3zptC9ApztFuaU8fHAHfjVCIV1Q4yjoPiwtPlUM5bJDtxFaK50U_tH_7AuPFh2gnrTOmeK3AjXfQBFr7wapaqDeEQhplBKgz20fWlkPd8414BvnmZkTuIBSqQ8t_NekB2QzS5WNZPU2rJCpTob5Xbf49yRE854Fl91962_MgHvG_-CxTQDg18MGDg',
        "name": '원 밖의 한 점에서 원에 그은 접선의 길이'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': 'https://blogger.googleusercontent.com/img/a/AVvXsEjtJexHxkGxDaRWqLKTndyafVagL2uXm4mnTMCJ-qprcFkjWo8e78FS7mKY5o1t8jsovpa_qFIvnl6v1eegcPO_kvGlyAveGIPiELMqFZ0aMlmnWvfX6ReaXWHuF3pU1OgWbfHg6r--2945bMsE8bQwU1A414CVXl-Ut2MVHQCuLRly1Hs--GnnLPQ-gg',
        "name": '원 위의 점으로 부터 거리의 최대와 최소'
    },
    {
        'category': '3단원.도형의 방정식',
        'url': '',
        "name": '제목'
    }
]


# 자동화
def card_list(menu):
    result = ''
    for value in data:
        if value['category'] == menu:
            result = result + f"""  
            <div class="col">
                <div class="card" style="width: 25rem;">
                    <img src="{value['url']}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{value['name']}</h5>
                        </ul>
                    </div>
                </div>
            </div> 
         """
    return result


# 부트스트랩 5 -> CSS, Separate/ Layout -> Example
components.html(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    <div class="container">
      <div class="row">
        {card_list(menu)}
    </div>
 </div>

    """, height=6000
)

#blog
#깃허브 로그인 j527ms@gmail.com,jms527527 왼쪽 eric 스트림릿 누르기, add pile, upload pile, 내꺼 고르기
#깃허브에 파일올리고 스트림릿 사이트에서 깃허브로 로그인, new app 클릭, 방금 깃허브에 올린 파일 누르기
