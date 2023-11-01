GetLGAFromName
^^^^^^^^^^^^^^

`GetLGAFromName?ABBNAME=COPPER%20COAST <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetLGAFromName?ABBNAME=COPPER%20COAST>`__

The :ref:`webservice-metadata` section shows how to get a list of valid council names.

.. include:: polyline-explainer.rst

Returns a JSON array of objects:

.. code-block:: json

    [
      {
        "ABBNAME": "COPPER COAST",
        "URL": "http:\/\/sdsi.sa.gov.au\/arcgis\/rest\/services\/DEWNRint\/WaterConnect_WaterConnect\/MapServer\/",
        "DHNO": [
          {
            "NAME": "PASKEVILLE SILO 1",
            "DHNO": 22710,
            "LAT": -34.0380586,
            "LON": 137.9017436,
            "MAPNUM": 642900006,
            "UNIT_NO": "6429-6",
            "MAX_DEPTH": 10.67,
            "DRILL_DATE": "1964-08-14",
            "STAT_DESC": "UKN",
            "CLASS": "ENG",
            "TITLE_PREFIX": "CT",
            "TITLE_VOLUME": "5791",
            "TITLE_FOLIO": "560",
            "HUND": "KULPARA",
            "PARCEL": "A",
            "PARCELNO": "11",
            "PLAN": "D",
            "PLANNO": "54180",
            "NRM": "Northern & Yorke",
            "LOGDRILL": "N",
            "LITHOLOG": "N",
            "CHEM": "N",
            "WATER": "N",
            "SAL": "N",
            "OBSWELL": "N",
            "STRATLOG": "N",
            "HSTRATLOG": "N",
            "LATEST_OPEN_DEPTH": 10.67,
            "LATEST_OPEN_DATE": "1964-08-14"
          },
          {
            "NAME": "TAC008",
            "DHNO": 290606,
            "LAT": -33.8842946,
            "LON": 137.8022206,
            "MAPNUM": 643001594,
            "UNIT_NO": "6430-1594",
            "MAX_DEPTH": 92,
            "DRILL_DATE": "2015-01-31",
            "CLASS": "MW",
            "TITLE_PREFIX": "CT",
            "TITLE_VOLUME": "5554",
            "TITLE_FOLIO": "59",
            "HUND": "KADINA",
            "PARCEL": "S",
            "PARCELNO": "118",
            "PLAN": "H",
            "PLANNO": "210400",
            "NRM": "Northern & Yorke",
            "LOGDRILL": "N",
            "LITHOLOG": "N",
            "CHEM": "N",
            "WATER": "N",
            "SAL": "N",
            "OBSWELL": "N",
            "STRATLOG": "N",
            "HSTRATLOG": "N",
            "LATEST_OPEN_DEPTH": 92,
            "LATEST_OPEN_DATE": "2015-01-31"
          }
        ],
        "Boundary": [
          "nkgmEglogYZg@}E}BAgA`IyJrJ}LxvBwKz_@mBzgAwFpmBwJl~AeIhqAoGfABfA@???O?CA{sCCsjD?o@?e@?aA?UIixG?S?UOgwHVwCY{AIe@??H?P?r@?fjD@L?H?J?~lA?j@?\\?l@?dD?J?N?J?j{A@l@?N?l@?|vA@D?jzA?~hCE|SA?UJavADcp@@aoAAaF?k@?gCA_j@piADzA@|W@hh@wLdp@Ifk@GvkAMzCA~|AMnm@Exl@Ehm@GttAK?B?PApu@Cju@?j@Arv@Ctt@?j@Anm@?x@?vP|Df~D?h@fAxhAhAvjA?V@TBlDJbJnBryBPhS^t`@l@`l@?l@~AlcBBt@zAx}ADxE?d@l@~n@l@pn@@j@f@xj@ClrAE|_B?h@Alu@Aht@@j@Ctg@AjZ?h@CpzA@vDGrqB?TAr_@?lUAtU?fF???\\?\\Azt@?tO?@AlA?@?vW?`C?@?D?|@?bAAf]Ab]?|@?dOCbf@?jG?z@AxX?jJ?vFEl@Er@Az_@IreB@^?^E`cA?z@?nAA`D?dA?N?T?tD?H?Do@g@OMc@[cAq@gA}@mAy@cA{@gAq@iAm@mAw@mAi@kAq@mAi@eBu@iBq@qBs@yAg@}Ak@uAg@cBi@yAe@cB[kB]{AUsB_@wE_AwCk@gC]sDWgEQsEUaDAuCCuBFkBTqBTmBHcBPgBc@sBg@oAo@aBi@yA{@w@}@u@uBLiACgA_AHRsF@KJq@BKCWIsAb@wA@Gn@{@p@g@FEA_@E_@?AOs@Ik@GQ_BkBYWg@]q@_@m@Yy@c@m@g@w@m@_@{@GIAAKKEC_@Qi@S]Og@Gi@QUE]EICm@Qc@Oc@Gk@Om@Ky@O_@MC?u@LC?GCaBoA?A??S{BJu@OI_@Mk@Ko@Qk@ME?q@K{@Oc@Cg@AWAc@NaD{@HcEP[@g@KGWIs@Mm@Kw@EcAEeACk@C[@u@@kAGo@G{@Ky@Qq@I_AIaAOg@E}@AaACo@C{A@i@Bu@Do@Bk@cAU_@M]EIY[SSUQi@Yo@g@i@q@]w@]s@Se@Wi@IUEAe@Gu@Go@G_@?kA@u@Ck@Ec@CG?a@C[AgCa@CoAEuA?[AKKk@Ga@EQKUYe@IUUI_@O_@Ge@Ig@Ii@Iq@Mw@Wc@Wc@Ui@e@_@c@UY_@]IIA?GAGAe@Dc@Da@Fa@?_@DcADkAi@c@k@OQSQc@e@W]UUSSSOe@Sm@]g@YWSMGOCe@Kg@UYO]MOGSICAk@Uc@Oi@Mu@Os@Sq@Ms@Ou@Mm@Si@Mi@Io@Ie@Ii@@q@G}@G[Ea@D{@Aw@EeAAcAC{@A{@D_AFaAHy@HgALcAHqANaAPcALw@H}@NeAPy@Lm@LgAXmAN}A\\{@PmA`@cARaA\\aAVkAZu@VgAf@eA\\mBl@mBl@aBn@iBr@qBv@eBp@qBz@eB|@aClAiAp@eB~@}Az@iAp@{AbAyA|@}AbAeBbAiBhAyBxA{AbAcBlAyAxAoB`BwBfBkB`BgCxB_CnBwBlBeA~@iBbB{AtA}A`B_A|@w@dAuA`BkDvEuBhDcCnDGH??JPtKnPvMnSeBTQ@A?g@JSBwAj@oAbAaBp@UNc@XOLc@p@QXc@hA?@Jf@RbAGdAE`AANGj@QjBGtBARIpCItDJh@DXNbAHp@Hz@I~ACFA@OVYl@EHORQTYf@GJOh@KZCFC\\E`@?~A??IhB]rAEj@IhA?BDZBN^jE@fABfBIzCR`ATdAFJFLCd@?BEt@QTORU^a@p@MfAEtAC~@AlB??ChAAb@??N|@Hd@B`@Bn@C|AC|AGt@Gt@QtBGvALx@Hn@Hn@\\bCMjACPOv@GXU`@MRYVI\\EVERQ`BYxCInCC~@Fn@Bl@HNP`@Rr@DN???T@PK^Ux@Q|@ADKh@aDrGIXGtAAZCd@Cl@Id@ETCTCLCBGHJV^z@QNONM?e@C[_@SWY]A?_@@OGIA??GGMOc@s@Qa@_@}@e@gCG[w@_BMm@UgA?qAA[FuAn@iB??@eADwA?AGg@?AGi@Ga@UCk@G_AJ?Ao@G_@E??OUMSEIA??S@cCL[fAwCCYK{@SsB??KaAOuAu@e@YCq@EC?cAD[JiAb@q@@C@W?_Bw@_CwHiFoN_JcQoByDcCaCuFoFwC{DoAcBuI_Le@i@kFyFkAeAuCeCdLwOV]?ACAuAYw@U]Gw@As@]s@[s@]QKMAo@E]@_@DiAXiB{@uA{C^_ACQMQW{@Kc@MWe@u@CGSuABe@Q]Ua@m@cAo@eBAmB?K@KB]ZqEx@JTBJYv@q@p@]?CJiAJcBV}AB]Fk@NoAh@sAb@y@DK?EEs@?GCQEa@Ia@GWAoBFm@D_@DkALwBJcA?_@Ce@Kq@Ou@YcAa@cA{@eAw@eACCUe@QOs@m@Si@GEe@[c@Yk@a@cAiAOaAYw@IiAKoATyB?ADE@?GIY_@k@w@w@q@q@s@q@g@oAm@s@{@e@y@Y]_Ao@aAs@kAq@eAk@gAw@k@_@s@Ys@Y}@Og@K_A@eA?u@@u@Hk@Hk@Lu@VcAPcAHu@Fs@Rs@Ro@Rw@Lw@LqAF_ADoAFs@JoA\\qAPyAA}AUmAy@u@g@eA_@w@eAc@_@u@o@s@}@e@m@e@]a@Wg@So@Ws@Ou@Ok@Ms@?s@AK?C?S?aAMwA[qAk@{@_@mAi@{@y@i@k@w@kAMoA[wAF_@y@q@q@{A[s@[e@_@m@k@}@_@aA]cAQmAO_AOcAGcAC_@Ke@WqAAKCIEWOc@c@u@WyASiAG_AM}@Mg@M[c@eAE}AA]CEYkALqAI_@}@{@[uDPSOOg@e@g@e@i@c@q@g@m@]eAa@}@_@{@e@gA]gAg@kAQ_AMuAK{AMwAMeAAyAB{@@eBDeBIi@?[PiAn@w@gA_@i@QUSMm@Ww@]_Am@m@c@eAs@u@cAq@kA{@mAq@_A}@oAs@cAi@u@s@w@m@i@y@s@w@q@aAo@uA}@wA_AcAo@_AaAs@s@g@g@s@s@g@i@e@e@s@u@g@cA[q@[e@[Yq@c@w@g@aAo@gA}@o@i@o@[aAg@u@m@_Ao@w@_@o@e@c@SgA[iAi@s@]aAc@y@i@y@s@{@i@u@e@w@g@_BcAu@e@u@w@_@aAKWW[g@i@o@s@e@g@k@a@y@s@KKm@SaAeBA_CCKOUWk@c@]k@o@g@_@{@q@CCi@y@_@o@CEYm@U]c@o@Ka@QYq@u@o@s@_AiA}@cA{@u@s@y@e@k@g@a@USa@[y@o@g@g@e@Wo@[oAo@{@}AAe@AEIIQYYYe@qADmABOA[Aw@LqAX}@JUFs@b@sAR[DOFSB[@CBm@F]AIEe@Kw@E[CSAIKQEKIQ??Qg@]g@[m@]g@a@q@EE[g@]g@a@g@k@q@i@o@e@e@g@[m@m@YYOK_AKgAoBMiBTeBHSEIWe@_@k@U]c@a@[c@g@_@c@o@]_@o@o@Og@CEA@EDo@p@aCyFR{@BMIQMgA?C[q@@}A@m@Be@?KEc@Ec@Kg@U_BYcB]eBQcAUg@[gAWw@Uu@Oa@I]AAi@k@e@_AYq@IOAAOK[WCCk@g@OyACOGqAC]CwAAOAq@Ia@Mq@Ko@AEAC_@?C?q@p@qBBmBg@Wk@c@Q[kBEiBz@iAJSP_@u@o@w@_@w@_AU_AQu@M[W^sMzSwBiOnBkTX_D_Bg@{FcBy@Q_DWaAAE?OAu@A{COgDKw@Cw@Cu@C]AiDBoBCQ?wB?_CF{CNk@BwAFcCJ_EXoDLoCZsBZqBb@yA\\{ARaBTmAJcALy@T_Ab@iAPqAVcAXc@LAFi@vBU@y@HHj@MdCsBfCgC_AYi@CCEAi@BQBqAPqARuBf@eCl@aCx@cBv@mBt@cBbA_Br@WNA?HLD`BIx@Ov@AF@vBWtA_@pAc@f@e@|@mAf@?BKZa@hBmBh@C?ML_@v@s@p@IJFf@AFOhBk@lA{@v@g@Za@b@e@ZMNOXUj@CFd@`@RfB@n@Fx@EdCu@xAm@t@g@p@a@f@Yn@w@|@s@d@EB[f@W^Sj@k@x@iAbAcATIBYHA?OF??KR]v@w@p@CD_@Zk@p@m@j@q@v@w@Zo@`@_@Zo@v@o@TCBYr@u@h@UNU^WX?FGb@AHJr@GdBYpA]z@a@`AY`AWl@Of@y@hAs@v@k@d@MJ[n@{@n@]PUpCQHFb@G\\WdBk@~@OTgAz@gAVm@XaATo@NYR]d@Wj@@\\AbA?JSxAkAlCcCCYICAa@M??OE_@[OCYCi@AkANiAO}@Gm@IWCSj@m@bB}CJ_@a@s@u@u@wAUoAO{@EYS_@U_@k@i@k@_AWk@O_@I{@Gy@]q@@_@a@Og@e@c@Wq@_@oAq@GEMQq@aA}@_Ae@gACIY{@g@yAO{AGiAB_@@YCYACKOa@[GEo@EmAc@cAe@cA_@mAm@m@]}@]q@c@GEqAkAUmBE{A????Bs@?OCOKYYm@IQ?_A?Y?k@Cc@CSAEEG]Ya@Yu@_@}@eAISQ_@CGEEUQm@a@UQ[W_@a@[Uo@g@s@yAAc@Ci@KI_@QGEq@o@AAWYSOQKWKy@a@QQYWe@Wc@Wi@Qq@Um@Uo@Su@Q_AOw@]c@QqBg@w@Ye@Ou@Q_A{@GQi@Mi@i@GI_@i@g@s@WqA?MASCCGK_@Sc@g@a@W[Ua@KuAo@OWi@Gy@ScA]{@w@US]MMIUAk@Kc@IU]a@k@Yi@Yi@e@i@[g@OMGEOCo@EcASgA}@Ws@MOWW[Yk@e@eA}@a@i@IC]A}@?y@QSGu@]s@YwA_Au@{AO[GEi@UcAoA[cAWg@AAc@y@Ug@W[e@e@s@w@Yq@IK_@Y]a@WQ]Q_@Oo@Sy@o@GGQSk@y@]kAY{@Ke@EIOMSMg@Om@[CAECUCw@Ko@Oe@MaAWW_@S[IIe@Y_@WAA[GaA]_AgAM[][k@cAGa@Ig@Es@_@Me@Oq@Oo@Yy@_@i@g@a@[_@[]Qe@Uo@[s@m@q@q@c@cAUgAAWu@Qu@y@m@s@Y}@c@Si@[eAw@e@yAIa@_@UYQ[Ii@Kg@Ma@KUEWGYIa@M_AW}@c@w@Wa@SWIg@CcAa@i@a@_@We@Yi@]cAc@{@y@c@i@OM_@Oa@O}@Uk@c@e@Ye@a@i@k@a@o@CC_@O}@]}@]u@m@i@_@CCg@c@s@w@a@eCRw@Lg@H_@DS?C???ACEKQSYUQk@e@EEk@y@i@}@WeAMw@Ey@ASCUCKKGc@So@}@KUEE_@[k@i@IMq@eASsAK_AEw@?KIGECk@My@q@MQ[Oo@o@e@e@[UUMEAc@SUK]Iy@e@{@cAKi@IGWMk@SkA{@Su@SUo@y@YkAAECKKE[Yg@g@CIMe@k@YGCc@i@IMEIKGo@W_@_ASg@Mu@]Ug@{@IO]McA{@IEk@_BAEKa@S[IKa@w@UcAQu@Oo@Qg@UeAA}AJiA@CF]EYBu@A[EEMQQUMWMUYa@S[QMSIq@Su@k@Y]QS?AS_@O[WsAIu@Gc@Ia@G]Ww@]y@[{@[w@[o@]g@g@w@a@c@c@q@QYSWSMg@_@k@_@c@[_@Qk@Sm@Uo@Us@Q[[[OIE{@u@a@cAWq@KWS[_@oAAg@[OMEu@U{@i@_@a@QQWQ_@UWOWIgAe@o@mAYsACo@GWMe@AEa@_@[c@QSECs@Yi@c@g@]]Y[[i@i@e@q@OWWQk@]UQc@]k@w@EEWc@a@o@OWSOe@i@[YSOu@a@s@k@WSOKUOa@WMMw@e@q@g@mAs@m@m@u@s@i@y@IKGKQMEC]Uc@Ui@Y}@w@GWk@Uy@q@_Au@i@eAYk@CMCAu@[kA{@a@aBOcAE}@Ce@AG????}@eA]y@Sa@Ua@[o@Ue@SSc@_@WUc@Ym@[w@a@u@_@[Oe@Uy@k@{@_Ao@cAWu@MYSa@Iy@M_@Ka@_@o@Ss@q@mACGc@_AQm@MSg@o@WWc@]KKg@y@Ug@_@_AWwAEo@AMG_@Qm@Wi@GKa@i@c@o@o@k@k@g@w@e@KKOMQGw@k@i@i@w@w@_@sAMi@KU]e@g@{@s@gAc@s@_@k@c@a@GGq@aA]}@?AIQe@gASw@a@cASq@c@aA_@{@IWCEa@_AY{@]m@m@q@}@}Ac@aAa@}@]uA]oBFK@CNSt@}@RWnAyApMsSnB_DZg@zMaT"
        ]
      }
    ]
