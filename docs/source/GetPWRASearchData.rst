Prescribed Water Resources Area (PWRA)
=========================================================

`GetPWRASearchData?PWA=Marne%20River%20and%20Saunders%20Creek <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetPWRASearchData?PWA=Marne%20River%20and%20Saunders%20Creek>`__

The query keyword of `PWA` is not a typographic error; it is correct. See the :ref:`webservice-metadata` section for how to retrieve the valid PWRAs (to use in the above GET URL).

Returns (this only shows 2 of the many returned "DHNO" records):

.. code-block:: json

    [
        {
            "DHNO": 72974,
            "LAT": -34.619298,
            "LON": 139.3815158,
            "MAPNUM": 672800080,
            "MAX_DEPTH": 34.61,
            "DRILL_DATE": "1953-01-01",
            "PURP_DESC": "STK",
            "SWL": 31.75,
            "TDS": 3583,
            "STAT_DESC": "OPR",
            "CLASS": "WW",
            "PWRA": "Marne River and Saunders Creek",
            "NRM": "South Australian Murray-Darling Basin",
            "LOGDRILL": "N",
            "LITHOLOG": "N",
            "CHEM": "N",
            "WATER": "Y",
            "SAL": "Y",
            "OBSWELL": "N",
            "STRATLOG": "N",
            "HSTRATLOG": "N",
            "LATEST_SWL_DATE": "1981-06-15",
            "LATEST_SAL_DATE": "1981-06-15",
            "LATEST_OPEN_DEPTH": 34.61,
            "LATEST_OPEN_DATE": "1981-06-15"
        },
        {
            "DHNO": 291276,
            "LAT": -34.7391396,
            "LON": 139.51077,
            "MAPNUM": 682801436,
            "MAX_DEPTH": 63,
            "PERMIT_NO": 254338,
            "DRILL_DATE": "2016-11-07",
            "SWL": 42,
            "YIELD": 0.75,
            "TDS": 2069,
            "CLASS": "WW",
            "PWRA": "Marne River and Saunders Creek",
            "NRM": "South Australian Murray-Darling Basin",
            "LOGDRILL": "Y",
            "LITHOLOG": "N",
            "CHEM": "N",
            "WATER": "Y",
            "SAL": "Y",
            "OBSWELL": "N",
            "STRATLOG": "N",
            "HSTRATLOG": "N",
            "LATEST_SWL_DATE": "2016-11-07",
            "LATEST_SAL_DATE": "2016-11-04",
            "LATEST_YIELD_DATE": "2016-11-07",
            "LATEST_OPEN_DEPTH": 63,
            "LATEST_OPEN_DATE": "2016-11-07"
        }
    ]

There is also the related `GetPWRAFromName?NAME=Marne%20River%20and%20Saunders%20Creek <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetPWRAFromName?NAME=Marne%20River%20and%20Saunders%20Creek>`__ query, which returns the geographical polygon representing the PWRA.

.. include:: polyline-explainer.rst

.. code-block:: json

    [
        {
            "OBJECTID": 4,
            "NAME": "Marne River and Saunders Creek",
            "PRESTYPE": "Water Resources",
            "LONGNAME": "Marne River and Saunders Creek Prescribed Water Resources Area",
            "GRO_PLAN": "429/2002",
            "GG_DATE": "20MAR2003",
            "GG_PAGE": "1111",
            "WILMAID": 583430011,
            "SHAPE.AREA": 743670075.299688,
            "SHAPE.LEN": 239612.608442263,
            "URL": "http://sdsi.sa.gov.au/arcgis/rest/services/DEWNRint/WaterConnect_WaterConnect/MapServer/",
            "Boundary": [
                "j{qqEmlmpYfZaf@~y@~ZFk@j@Sj^gN`VeJl}@}UjBiKJg@l@yCj@Ixc@uGjPyy@zt@rUyA~Ke@rRKj@rSkAxVeUdCOb@CzfAyHxG_\\tCwA|XfJn]hLd@N~DrArOhFpAs@zYzBlMsB|IwAxLbFc@zS~IvFbQMxPOvGElCbDrDtAr@VzBi@b@M|CeErFmLpEgMfByMtC{TjBiBfFyPYcGgBoEqMrCgCSeBqFCuC`D_Ib@}A`Bm@tBgBnAgBz@kBEcBp@iLj@eET_MxDBd@}VkAEB}CUoDyBmDQ{Abe@JnRDsGuZjq@iAsAmI{EyY{Gya@qEAwb@IJqu@nb@qDpEuA`VtEbLOb@cCdDgQbCkMJm@Lys@@q@Ju}@Jcv@?i@?uDHyi@Jgn@@wVDq@?w@Aa]?mQb@Bzq@jEAq@Hkc@Nku@kr@Yi@?RiqAwj@M@k@TwpA{k@Ce@?AhJqx@KIuaAcXGSk@~a@sdAuh@K^{aB@k@|i@JDsbAuo@HF}}@cr@NBg_AfbB@Ai@@c`B?y^dp@?b@@C`e@hz@BtX@fw@Bb@?lAiSzn@E`J?XokB`cAyJCk@SakBrQAFe|@?yGDet@Bm`@Am@I{tAd@OvhAVd@BaGw{ACu@sBmi@oD_~@C{@Pyb@?wD^sbApn@GQ{eBrZIIge@AiAfF`Jz[z_@bZxRbDqI`@iAXLFDLNNHTRb@Lz@XbA^r@N^Jn@Lz@Vv@Tb@NObAmDnR`BnB[b@oI`L_@b@vHtg@hSvsAXlB|f@~`A~k@hiAd@~Bd@CpfAeCRtdAfgAKNtvAih@Y`e@t_@_AhBoLdVpUnR`Ad@zCfCL|_Bex@DoH?im@D^hkB\\h@?j@sS?TxbBqu@Fl@|~Bsb@Bc@?ml@D?z@?llB?j@ef@EfMpu@xTfrAu_ADc@??j@?n_Bd@Bxv@BAp~B{AF@j@T~aBbaA@lM~mAEj@o@vAiDp}AaBju@b@?bgAc@mSup@f@Anp@AIqxADk@Ec_AxbA}f@fbAuf@vWqMb@U||Asv@hWmMb@U|c@{ThEqIpMkPjA{AnEwF`@qAIc{Bdw@aOjw@cO|E_AfAaAu`@gf@Bsj@xlAFb@?zfAP?e_@@ql@@m@Hov@`m@GN?x\\ElB@fp@AAcfBfi@B\\i@pTCr@?PcANwCWuBJgB?eFC{Eq@cE~CiKRs@tAa@A`A@Z@Z?`@?\\@\\@l@@R?^FXNd@?Z?VA`@D~@DXH^ER?R?VDPDR@P@R?^?T@T@`@Bj@@b@@ZB`@@`@F`@Bh@Bd@Bb@B`@Fb@Dh@@ZDn@?TBP@P@j@@^DVD`@@V?TAZ@Z@r@B^@`@Bb@@\\D`@Fl@@Z?VD^Df@Fb@@TA\\@XFXDX@b@BVBZ@`@B\\@\\?TBVHJJXFNDJDT?P?RANARAN?N@F@b@@PBT?V@\\BX?D@J@N@HBD?\\BP@R@TDR?R@\\@RBd@Fb@Dd@@b@Db@@TDd@BXD^Dh@B^BTB\\BZDh@Db@Bf@BTB\\@RBR@RFb@@RDf@Dr@Dl@Ff@@L@JB^@ZD\\@VDVB`@BXBTBZBZ@LDB?DCD@FBT?N@?BV@VBX@RBD@B@D@JDPFVBHFPBJ@LBP?R@P?T@L@LBP@LBJ@N?PDR@LBPBP@JAHDNB\\@Vi@ACBBZ@J?NDT@T@VBZ@LBVBVDV@RBRBNHr@@PBTDZBJIpAAn@XvE?@@PB^Bb@Jn@Hz@TtABTBJFf@Ff@B`@Fd@Dl@Hr@Hd@^fERpBp@pHNxA\\|DNdAf@bEP`BXvBRzBHf@RlBHj@BP@PDJ@TVtBZtC^nDNtAJ|@RhBJ`Af@pEBVT~CF`ADf@J`Bd@jARd@Vl@x@jBP^LXt@zAR^LXJRPb@NXFHTn@R`@HLHJLRDJHNLRFLFJHRFHHDDBLDgBxA`@bA_@bAIT_L`[a@tAgDjLi@QiKqJ{ApAmD`DaAzA}AvAqAz@qCR}@P]HHXs^|e@sEbGgGz@}ObRGxAoA~Am@vBRjMc`@rg@qHjOoCpFSb@cOlZwAtBeKxFgv@B{m@@Gl~@lG~e@e@?_t@?IrZkr@@Bh`@Gj@?pT@ddAJj@O~aADzp@p@qAb@VwCp\\oBvKi@vByPrVVtw@b@`pANxd@?f@Vlu@T|p@?j@Tjo@Nne@DrMc@?{U?wFi@wE??h@?FA`a@?h@AlS?fCqUTyHbFoA^SxEmC~l@m@zMiDpv@w@bQ{Blg@aDjs@cEt}@_Bh\\g@Cwe@oBy@d]}Y}ACl@}@hYDhBYvDk@dQN~ElAfElFpK]h@ZpCrC|CbDvGZp@lDhHjHhRnAtFhEfRx@`HSjH{@rCyVvm@eB~PhAtDqMq@sY}AgSeAa@ACj@qAva@mh@uCyA`a@Ej@yOoF}VsI{Izc@yIrc@Kh@mCzMhFp[i@QqKsDa@OwIrc@cNsEyHxJ{C|D[^MMiFwEEYMMMTQOJUuEcEkFmBeBo@oEeHcN~q@eCbMhTbHxGvB??xQ`Nb@`@{LjEEtA_@~Q}A~FiEzDS~NC~AoBfGWa@aJkAkBAS?_DfA_IdBeJj@a@DmH`BiH?aGf@qDtBsC|@uBFuAo@mAm@mDWoC`AuCzDgOzJ}@d@yFcAcGgDiNlFkI@oDxEeOhG_CzCoBbCiBxBcKwAgE_@}Bv@y@n@aDdHiChf@WZgHzHgGrM`D`Qq@jIGl@wMzDoK~CgJlC}Ex@e@JkAbB_E~A_GhKeEhEc@ZcE~BkEpCaDbA{MpGWNwI_AiBo@c@OeBj@iMYyEXq@Dy]xDyF_Dc@GeHcA}A?wFFsDNkEh@yIzF}KjB}OEiBmAiDn@q@LiBBc@?{IeHwKVg@bACH@J}FyFuIpKUa@}IwNkB}CeEaDZuAhAaFNm@zBcMqC_VsFoNwBmc@oKa]w@gCcAkBgCsEsGsa@@yBBw@P}@rJ}d@i]aLH]zBwKb@sBNg@fCeMJi@Jc@Ny@zAh@jBn@rAgFjGkE~EcM|CcAfBgDaBgFlDoG{DgAcDhBKGkAa@kGaCpFqWnDqJ_@sKwGcFOoAoDaE{ASW}@y@yAuGaFBg@@uCm@yC|H{Ij@oGgIcDwKoCwG}KkN_J[sGU{@YeAkDyM{T@}AzCYFmO`DaObBeC}@YM}CwHwEoAaTdDaQlCgMeJ]YkCkBoHNi@jE{EvA{CyCwDwCsH}FgFeCcGzHoId@yHrF_@t@qI~KgKb@wIdNsKKqChIc@nA{JgAc@U?CkFg@iFaBeEqDqQ]uLuCuMl@_PsHIyPaGuF]GyCqFuLxF{C]b@cHsF{N_HkEmDsA_DmAqIv@gCz@{FfDuR}@gZ_J_@KgIgCeQqDa@uC{VpJUU][_PwNyAiKeNw[yF}CiG_OSg@oDeIsHeCgFwCsE_A??mFgAmHaFaJuCeBEiFuB}I{BwNwCmB}DwHqDa@SgEsBu@_@LiFvCaGlAsK}AoHb@gNxEuEVoIcGiKgFcK]]t@yIzDiEuCsKwCi@sIn@kEaCgCoC]yELi@`Gc\\{j@}QqAgSdGwShIgIpCrDVNzE}H"
            ]
        }
    ]

.. include:: footer.rst