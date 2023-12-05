test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


prod_data = """
seeds: 202517468 131640971 1553776977 241828580 1435322022 100369067 2019100043 153706556 460203450 84630899 3766866638 114261107 1809826083 153144153 2797169753 177517156 2494032210 235157184 856311572 542740109

seed-to-soil map:
1393363309 644938450 159685707
2025282601 1844060172 19312202
1233103806 1026919253 32871092
1086566452 1933428941 86530991
1265974898 0 21589659
1357621124 1636167265 35742185
2343571960 2665606060 81121142
1585337376 809179011 202497192
3151050390 3039622538 54531851
2059837853 804624157 4554854
169037772 124717914 59280146
228317918 183998060 248114943
2646529073 2343571960 51673623
1173097443 1360585007 60006363
2000660015 1203115155 24622586
1059486394 1176035097 27080058
3129081851 4185259485 17367169
3599437884 3098755759 211817367
2810085327 3883695720 116314513
2424693102 4015066563 32329632
3398847262 2507128214 141172870
1787834568 432113003 212825447
1553049016 1603878905 32288360
3111414816 4202626654 17667035
4015961437 3493485543 279005859
3584381554 4000010233 15056330
609280127 1840486939 3573233
0 1603418622 460283
3302297495 3310573126 79244791
3811255251 4047396195 137863290
3381542286 2648301084 17304976
3280255848 3389817917 22041647
840113387 21589659 103128255
3949118541 3816852824 66842896
3205582241 4220293689 74673607
657286135 1420591370 182827252
1287564557 1863372374 70056567
460283 1671909450 168577489
2926399840 2746727202 103388997
3146449020 3094154389 4601370
943241642 1059790345 116244752
476432861 1227737741 132847266
612853360 2019959932 44432775
2698202696 2395245583 111882631
3029788837 3411859564 81625979
2044594803 1011676203 15243050
2457022734 2850116199 189506339
3540020132 3772491402 44361422

soil-to-fertilizer map:
1845319553 827629590 305617985
3122295925 2644420892 346256096
1459294850 681645131 145984459
1609507353 0 58999651
255693782 1322254706 15503402
1136906676 1310560683 7032394
609209731 1833691163 45329504
271197184 2213414186 148369535
3483324631 2990676988 343929863
3943098203 3619829050 148418709
2945015193 3803447520 177280732
504622935 1337758108 104586796
2644420892 3334606851 81771815
2909815432 3768247759 35199761
3468873015 4096571961 14451616
3827254494 3980728252 115843709
1044649784 1218303791 92256892
3468552021 4111023577 320994
1605279309 677417087 4228044
1668507004 58999651 176812549
978403972 1317593077 4661629
212737043 1879020667 42956739
916089003 1655081947 62314969
0 1442344904 212737043
1228536146 2361783721 230758704
419566719 1133247575 85056216
1143939070 1717396916 84597076
2726192707 4111344571 183622725
983065601 2151830003 61584183
2150937538 235812200 441604887
884391832 1801993992 31697171
654539235 1921977406 229852597
4091516912 3416378666 203450384

fertilizer-to-water map:
2549847515 3576009818 718957478
0 241538153 477666033
2425421388 2487425840 6333278
2431754666 2369332991 118092849
4172623904 3453666426 122343392
2050888028 0 241538153
2369332991 2493759118 56088397
477666033 719204186 1573221995
3268804993 2587418451 866247975
4135052968 2549847515 37570936

water-to-light map:
0 614660468 46162263
992982309 3320291957 519425172
2148695908 4242883656 34662742
2183358650 992982309 1749887545
622053693 575891430 38769038
1973119806 3839717129 175576102
3950667093 3281596434 38695523
46162263 0 575891430
1512407481 4015293231 227590425
1739997906 3048474534 233121900
3933246195 4277546398 17420898
3989362616 2742869854 305604680

light-to-temperature map:
3926915598 4278168812 16798484
1868013910 2147559018 140836186
750719301 1001446770 132766166
0 591148217 159571084
2757723179 3756680674 111319765
3526572182 1656447494 400343416
159571084 0 569934147
2869042944 3868000439 358532427
2008850096 3039560686 189896094
2649579616 3734175051 22505623
2270874649 2588070691 164667420
4008144721 2752738111 286822575
2435542069 2374033144 214037547
2672085239 2288395204 85637940
3450693140 2056790910 18639649
3469332789 3452574549 57239393
883485467 750719301 250727469
3943714082 3509813942 64430639
3227575371 3229456780 223117769
1708083440 3574244581 159930470
2198746190 2075430559 72128459
729505231 569934147 21214070
1656447494 4226532866 51635946

temperature-to-humidity map:
2530950430 2986195732 64296956
3097031068 3050492688 225336526
2595247386 2262922844 63415061
394235114 386308291 573314459
159338027 199058685 71729011
2107189180 2969998741 16196991
231067038 0 22309581
266735072 959622750 109765613
1941982137 2514902112 165207043
3525862760 2680109155 81512917
3809165514 2049071587 78022870
3887188384 2459869958 55032154
61551861 270787696 97786166
4083271930 3575006611 18595319
993228240 162831557 10548461
967549573 173380018 25678667
376500685 368573862 17734429
2877832272 3856947724 19626311
3607375677 4093177459 201789837
2519444451 4007134226 11505979
2658662447 4082384303 10793156
3322367594 3945539199 61595027
253376619 149473104 13358453
0 87921243 61551861
2961202681 2127094457 135828387
3942220538 3468929261 33142375
2669455603 2761622072 208376669
4197950728 3371912693 97016568
4101867249 3275829214 96083479
2446763340 1976390476 72681111
2313231287 2326337905 133532053
2897458583 4018640205 63744098
2123386171 3667102608 189845116
1003776701 22309581 65611662
3975362913 3593601930 73500678
4048863591 1941982137 34408339
3452927785 3502071636 72934975
3383962621 3876574035 68965164

humidity-to-location map:
0 853712401 14149303
2655090225 1087300934 303915897
2027272660 3174210041 18998832
1525779414 1936221923 38337972
4147713982 3193208873 142508118
2959006122 2143904256 380930882
1087300934 1765319513 65896883
1352738345 4121926227 173041069
1290854129 4060042011 61884216
3931908769 4005664051 54377960
4091732209 2524835138 55981773
653782902 95274560 214078802
477505648 85866717 9407843
2632545935 1543458967 22544290
123251703 309353362 97540905
3762564408 1974559895 169344361
3487433944 3409639319 23582322
318179985 430129950 159325663
1216931801 3335716991 12046317
1153197817 2580816911 63733984
14149303 406894267 23235683
2206646140 3433221641 320894268
3986286729 1566003257 105445480
37384986 0 85866717
2112775364 1671448737 93870776
2046271492 3107706169 66503872
3511016266 3754115909 251548142
1228978118 3347763308 61876011
1564117386 2644550895 463155274
3339937004 1391216831 147496940
486913491 589455613 166869411
4290222100 1538713771 4745196
220792608 756325024 97387377
2527540408 1831216396 105005527
"""
