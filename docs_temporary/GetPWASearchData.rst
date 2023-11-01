GetPWASearchData
^^^^^^^^^^^^^^^^

`GetPWASearchData?PWA=Northern%20Adelaide%20Plains <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetPWASearchData?PWA=Northern%20Adelaide%20Plains>`__

See the :ref:`webservice-metadata` section for how to retrieve the valid PWA names.

Returns a list of wells as a JSON array of ojects:

.. code-block:: json

    [
      {
        "DHNO": 27192,
        "LAT": -34.5875312,
        "LON": 138.4141681,
        "MAPNUM": 652800049,
        "MAX_DEPTH": 243.84,
        "STAT_DESC": "ABD",
        "CLASS": "WW",
        "PWA": "Northern Adelaide Plains",
        "NRM": "Adelaide & Mt Lofty Ranges",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "N",
        "SAL": "N",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_OPEN_DEPTH": 243.84,
        "LATEST_OPEN_DATE": "1964-02-03"
      },
      {
        "DHNO": 304120,
        "LAT": -34.6118451,
        "LON": 138.5221818,
        "MAPNUM": 662829233,
        "MAX_DEPTH": 68,
        "PERMIT_NO": 292866,
        "DRILL_DATE": "2017-12-07",
        "PURP_DESC": "TWS",
        "SWL": 11,
        "CLASS": "WW",
        "PWA": "Northern Adelaide Plains",
        "NRM": "Adelaide & Mt Lofty Ranges",
        "LOGDRILL": "Y",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "N",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "2017-12-07",
        "LATEST_OPEN_DEPTH": 68,
        "LATEST_OPEN_DATE": "2017-12-07"
      }
    ]

GetPWAFromName
^^^^^^^^^^^^^^
    
There is also the `GetPWAFromName?NAME=Northern%20Adelaide%20Plains <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetPWAFromName?NAME=Northern%20Adelaide%20Plains>`__ request, which returns data for the geographical shape of the PWA.

.. include:: polyline-explainer.rst

.. code-block:: json

    [
      {
        "OBJECTID": 13,
        "NAME": "Northern Adelaide Plains",
        "PRESTYPE": "Wells",
        "LONGNAME": "Northern Adelaide Plains Prescribed Wells Area",
        "GRO_PLAN": "429\/2003",
        "GG_DATE": "13MAY1976",
        "GG_PAGE": " ",
        "WILMAID": 641834400,
        "SHAPE.AREA": 606769218.58595,
        "SHAPE.LEN": 137189.4653942,
        "URL": "http:\/\/sdsi.sa.gov.au\/arcgis\/rest\/services\/DEWNRint\/WaterConnect_WaterConnect\/MapServer\/",
        "Boundary": [
          "zlisEgbtlYDWJ@LEAQWTOFSd@CNHx@THBbASSg@FYXQdA[RWGCTFDLPHl@JNIJMPQ^_@Tw@KBQKSMNMf@IFYdAm@nA_@\\FRGf@CTi@l@a@NIJq@Hy@Ri@x@Gx@OHOSGOUSILa@AO?MX?PEN_@CURODCNFL?PUAq@?[QKGUHCRDXMJy@?WRQAEMw@a@k@Te@TD^SX[Ua@FMlAENYBIZNh@QBq@t@u@r@g@DUIILIPWMYFs@h@_@x@[QW@OR_@As@b@k@BKCcBdAk@CQAUe@k@UOi@ME]^s@r@Qn@S|@OI[TO@[c@U@ISKD?R\\|@DJKPEXSUWPKW_@D]\\aAv@SYO?]s@Oz@GH]YWAUU_@AKICuCDk@\\eATe@`@ULUfAs@OMA[[Be@Kg@DKEk@PiAnCyAHyATM@_@UKN?b@?f@Hb@AJs@l@UCOeAIEW@cBnBm@Be@Qe@PGd@MNs@V{BW[S]iBmAsBOoAIWD_Cb@cBEOiA`@}FlBy@p@g@`ASF{@q@q@mAe@YgAS]_@mABeAfAOBi@HeATw@Li@DQCkAdA[BOIMJ?NCZ_@SOEy@Ha@VWAWLNR@HQDg@WQ?Ed@MJC`@c@TSC?VFFARODSHKJEZTTa@b@q@ZOBW_@h@m@h@O?Y@c@i@Q{At@MfALNQPOVMDIKYAa@Rc@Eu@BMh@u@f@y@JeBmABUi@j@e@HOIQFsAb@gBh@oAtBoC~Am@W?m@QMQIMJUCAPa@l@h@HJSFGFB?`@BZObAFVENiA?k@VG`AUx@y@LCOFm@Wu@o@CCYIEwB|@Yj@sBnBk@pBUPO\\?Le@Pq@p@s@QY_@WE[|@c@p@S@_@Pg@JIOQ@O@MCGJHPC~@o@XWIu@b@IVSNOTODYRUFMH[DQFQFQ@MDMBMFQHQ@O@[BIFc@?k@NMB[HSJMHKBSJODYFSBYLKEKJMBM?Q@KIOBOBa@POAUHYH[DYBUEQCKDUFGHKEODUFM?WZMBOAMAK?KHEKwCaGSa@MJOLMLWPUPUTUN]Xu@n@m@d@k@h@i@^c@\\g@f@WRQPWPUPm@f@i@b@m@d@eBjA[Za@^STg@d@[L[V[NWL]TUTSTi@j@g@h@sAtAyC`DWVMNk@l@i@f@g@j@i@b@_@VDL?n@}@nBk@fAc@z@m@bBa@`Ai@r@w@rAa@z@m@jAi@|@i@vAw@pAc@dAs@`Bo@lBKv@ShBMzAQtBUvAW~AUvBQbCKpBSbBGdBDhB@bBEtAFdBGbBQbB[pA]|Ai@bBu@fBw@tAq@tAaAbBaAdAu@~As@hAo@t@[r@g@fAg@|@q@lBm@lBc@zAWpA]pAIdBEhACtAAjAIbAi@|@c@b@[x@c@dA]hAg@jA_@~@InAWhAGz@Qj@MF]t@Wx@Id@Q|@Al@SZSLm@LQp@Bt@Nt@Hj@Lr@O`@[Jg@Fg@j@Ux@S|@c@d@c@p@MvAUv@O~@k@fA_AnAm@vAY|@UbACr@i@Xm@Dg@Cy@Lo@?q@Jy@l@y@lAu@t@yAx@uAdAwAdAw@z@s@r@cAfAu@p@i@l@s@z@oAdAgAn@mAxBu@jAc@n@o@z@W\\_@r@[`@a@l@Yn@[t@_@l@YR{@f@y@Hg@Fk@NaAp@y@l@{@h@cAZeA`@{@Lw@`@eA`@qAl@}@d@iAj@o@\\k@XSXa@x@O\\O`@OZ]Zi@\\m@~@]d@Wr@Wr@a@n@gAhAcAr@_@v@u@`AKTUd@KfAKz@QjAG|@GhAAz@?r@Cj@]n@]`@k@Ve@LyAF}@V}@UsAo@eAk@}@Uq@Aw@J_AVq@Vm@Nm@Ls@Kq@Hm@Zc@V[Zo@h@]v@i@f@Qn@a@r@Yx@On@Yz@Up@Y~@a@~@Uv@w@n@Wj@Sh@Wn@Fp@ZhA`@|@Th@V|@Td@Br@Nd@?r@@jACbAK`AMp@_@z@Wr@i@^g@n@]d@e@\\]b@g@\\SNMZRd@n@\\r@Xt@Dp@Rh@?\\Fh@PVV\\JNd@Hh@Gr@Op@Yz@Wj@_@p@c@h@g@Z_@Xy@HaAC_A?o@?y@Ey@Cq@Ey@@i@\\_@Va@d@m@l@W^c@b@g@d@e@Xk@\\}@n@u@v@m@l@m@\\_@n@g@z@m@dAWbAa@nAMbASpASjAYfAMz@g@t@i@|@w@`Aa@`@c@r@i@b@q@T}@Rw@I_ANaBEoBGwAKuAS{@OcAMgADk@Rm@Hq@n@g@n@i@j@g@r@i@x@Yd@SZq@PeA^_@Th@zBjAjE`ArD`@~Ai@F_@Bi@Da@PWHg@G]CYJa@b@a@^YVO\\?^M^WTWXGZOZ[PSd@UP[VERFVPj@B^Ib@e@VK?g@Pe@NaAl@gA~@m@n@q@z@e@j@q@z@_@r@e@z@c@~@k@`Ao@nAo@dB]fA[dAUt@Qz@M~@Wj@[l@Sh@Cl@Ir@Qb@Qf@Yp@[b@MRc@Vo@BYEOHU`@EXI`@?\\Vp@Jb@DZI^UNe@LSZi@\\u@f@kAt@aAv@k@\\k@Pm@Ho@^w@`A[p@]`AE^AZ?LBNJ^Vn@F`@G|@_@p@MBUA[Cg@Ko@@e@P]TWRQBWJEZA^Sd@c@h@_AdAMBWIe@Ca@\\W^Wl@On@i@p@Qf@SlAM|@S~@WpA_@v@i@r@q@`@eAHo@R[@e@HeAJqABy@Go@TaAF_AAaA?gAWc@s@c@s@i@Wa@QOc@U_Am@w@g@m@[A_@GmBeA_Cu@kCmAkCuBgBoAsBcB}A[iA[w@Yi@MyAKcACiAGk@Kg@Yi@_@q@[s@a@y@[wAo@gA}@m@wA]_AOq@Ay@?o@Da@Cu@?k@G_@Da@@WF]@qAAc@@]Zi@`@Ul@Qb@a@b@g@x@w@f@]`@m@Zu@DaA?eBHs@@y@Ss@SeAGe@?g@Ks@Mi@_@cAM]Ie@A]Se@MSQm@kDkAsAbAoDbBiKrAaKbDq@ZmYjNk@RiDhBuDpBoKfHkRbKcMvGcMvHmIbEmG`E}HtFuLxJuLtJuFpGwFpJsAxCKdDAn@AhAEjA@bABfB]bBmBhIag@rQaF`B_A^]Do@l@WV_@Dc@Fc@He@PkATq@Pi@Jk@Tg@P_@Jo@T[Lc@FMBQJ[Xg@NYNg@NK?URc@N_@P]L[Nc@V[JSBMHQRc@Ra@Rc@TYRWLWNq@d@WLUVi@Vg@\\c@Ta@Xe@Ve@\\]V_@Zg@Z]Xa@`@ST[TWZ_@^[XSTS@URY^k@Zs@f@eBlAYxAYXW?s@NmD|CgIdJ}ErF]d@_@d@{@xB_AdDKZG`@Oj@Ih@O~@EhAIx@AbBGtAAh@BTFJFJFPFVJXHT?^@\\BZ?\\CZE`@KXQJOLWVOJKJDnRgFbLmIxGeATuHfB}EzFaKc]wAkgAEgOU}PYaV_@gYa@qX]_X`@YO{Mg@ma@k@og@cBktA_B}sAgAw~@iAi}@o@uj@Y?cAyDPgBt@qH?_@_@}TAq@yAklACi@@OGmBg@}a@m@se@Eo@m@ye@m@}e@Ak@WwVQ{Vm@ap@A}@w@ijAFMGo@MmMKoMGwHc@we@?k@e@_f@e@gf@Ck@a@_f@I_My@yx@?w@w@g{@y@oy@c@[us@@qZ?e@CcRBs_@Bk]B{@G{s@Hwx@Ji@Gi@?e@B__@Aq_@@a@A{gABDaACsbA?kl@A{k@Eo@Bwq@?k@Ago@nEav@pEyv@?m@nCgt@C{C|E_cABm@zD}x@|@sR`C}e@?i@pA{W~Cmp@e@GWA@i@lDas@B{@NmC`@gIdw@|E|CT|EZXBf@Bp@Fh@Dl@D^Bd@@n@Fj@DdAFl@Dl@@vANf@BxAFzAJ|Fd@l@Al@Dp@DrAJlAHl@NhADhAHn@Api@nDrJp@b]tBp_@~B^Tf~@xGxCQAVb@DB[LI~ESMrA~DXzC`BzB`BrAxAt@l@zDdFpE~FZ^ZCx@fAQRxEvGDu@jB~BvEdGHj@v@v@|@|AfFeAj@KxA[l@Kr@QtAYvAYJHbAb@j@j@b@\\l@j@VR|@v@ZXZZ\\TVXZXh@d@XXh@b@b@\\b@^\\\\`@\\\\ZZX^XXXXVZX\\Z^XZX\\ZXXZZh@^d@d@\\XZX\\Z\\VX\\NLNb@Zp@lG@vCIpAJzDnAn@RlEyCrCmBRM~PkLbE_Cb@Y~BcBxBoAd@}@JK`Am@t@i@^S^ShAq@`Ag@bBy@bFmBrG{Ab@I^EfCvA^PVTTJ\\VVZZVTXZZTVXXl@v@Xl@j@AbCEd@Eb@@hAE`@?b@Af@A^C`@A~@jAX`@Zb@Zb@Z`@f@n@fAvA^d@^d@f@p@f@r@d@l@h@l@h@t@l@t@jA|Ar@z@\\f@VXT^Z`@\\YpBs@`@OlA_@b@Qb@Md@Sr@Up@Sp@WxAe@f@Av@Mb@Cp@EZELAz@Ep@Ir@CpBOjBOhAKpBI^IVCd@Cj@Ex@?IYMU?]AM@_@?M?Q?M@QAuC?i@@g@Ae@Bi@@m@@yBHe@@y@CeCv@n@\\VVT^X`@^RNrCzBXPhDlCdBvA`@Z`@XrFlE^ZlBxAtBfBf@\\d@^\\VHF^X^\\hBvAvB|DbG~BrCzBnj@lc@l@d@|GpFhPnMrYlUZZMVhCrBfBpA^\\VXlDhCbCnB|@r@`@\\pCzBjEnDZTxB`BzBbBxBfBrFpEb@VL]pY|TJFd@`@L@tI`E`LlF|JtE|E|Bv@`@tB~@zBfApGxCxN`HrB`ALi@dD~Ax@^zIxEv@`@pFxCpB`Af@Z|A~@b@T`Ad@VLNJXP\\PXLVN`@Rd@^XJr@^ZPTLXLZNXPVLp@^x@b@h@Z~Az@j@\\jHzDvAv@^PtA|@TD~CdBhFpCt@d@nAn@|Az@vHdETJlBfAnFtCrJlF`ExBdAdADJ`@Jd@Xh@Xf@^HAf@Xb@X\\PZP\\N\\Tb@T`@RVPb@TRLHRrDnBTB^R`@P\\T`@R^T`@P`@VHHd@Tj@T`@T^R`@Tb@Vb@V`@R`EzBHD^R`@T\\R\\R\\NZP^R^R`@TRJl@ZVN^PZR\\P^TdB`AhE`Bv@d@p@\\VHb@X\\NZPZP\\R`@TXNFF\\L\\T`@RZPZTZPb@Tf@Xl@ZXL^Tb@TVLFJf@PTJVNd@VZR\\PZN^R^TfCrAFJd@NJFfCtAHHLFPJJNFHDJdDhAN?r@TxBZdAHLBrAAbEQxBYtEg@LGzLyAxe@}FTAhBQNI|@M`Gs@nAGJ@r@?^Cp@Fr@FJ?p@C|@Ch@A\\?d@A^?h@CZC`@A\\A\\Ab@Af@Ah@Cr@Av@CnGi@RClRc@rEFbBKTKt@G^?R?bISj@Bx@?xBOrFO`BCb@}DRq@TaAZcAVu@\\eARy@Ng@L_@Ne@Ja@La@Lc@P_@He@L_@Pi@Tq@DKLg@R{@Rm@L[f@y@gAi@QIUI_@SSGMIU]g@_AA}@?]C]Cg@IgEDeD@eAEs@Cc@Gm@Ko@K_AAIVqEzCaD`BcB~AmHzJ|DjFvB`D~A~Ax@nCtATHBK?[D_@?OBSDQBQBQDS@QDYBODK@QDSDMBWDS@M@M@OAM?MEO?OEWGSCKGQGKIKEMKMIKMGIKKGGEOSCSEQAMAUAQAQBIAMBUDUDMbKnDnUjLXNfFbCtGdDlCnA^PHGx@t@t@r@`Av@zAvAh@b@ZRb@b@n@j@l@f@j@d@f@`@`@`@b@`@|@p@x@t@tBlBXVr@h@v@n@bA|@`@Z~@x@^d@dAv@t@l@CJ\\XZV`A|@@MdAbAbCpBPX\\XRLNNTTPNJH^NjAhARLt@p@ZV\\b@j@^^Z\\\\\\X\\`@t@f@TTXTTPXVZXVTXTpB`B^^DRb@b@ZTXT`@`@ZVZX^XXX\\Z\\TXXZX\\V\\^LHp@j@b@`@ZV`@\\^ZXX\\XVT`@^TN\\Xv@r@VTNThAt@HH^\\`@VNTf@^h@b@\\X\\Z\\\\\\VZVNNFJf@\\d@`@b@^^\\ZV\\X`@ZZXZX\\Zr@l@`@f@LDn@h@JJZTXVZXRT^VRPZXXXXTXT^Zv@p@t@n@XX\\T\\ZXVFLd@^NJ^ZXT\\\\VVXV~AtAlA|@XVXVRP\\^ZRXVLHJJ^\\f@`@xArA\\\\\\T^Xd@b@~ArATTZTPR^XZV^ZFf@PLXh@d@b@v@ATVXTZV^ZNNHJ^\\b@V^\\ZX\\XXX\\\\\\\\\\\\V`@`@n@jA\\^X`@\\XVLJHJnDxCVV`@ZVRZVXVZXZVRRn@n@RLZXZTZXZVZZZXZV\\Z^XZXXX\\V\\XZXZXZX^V^^l@\\ZTZX\\X\\^JNLNl@l@ZVrAdAn@l@XTXV\\XXTXXXTXVXXRPj@d@NLXVXVXRZX\\XJJnAt@vIvHnFrEp@p@ONfDpCHUdDrCpTfRjBn@fM|AxAh@`Bp@|ApALh@TNVTVVh@d@h@d@lAbA`Az@HOd@^nBdBZVd@l@bFbEpCbCj@d@PV~ArAXN~@x@\\VXXXRVX\\TVVVRTR^`@XVVNVV\\XVTXT\\XVVZTVVVVJPLHHHj@b@ZPZXZXXVX\\`@R\\^NHLLLHLNZVZVXV^^RTZT^VRR\\ZZTZXXX\\VXX\\VZXXV^\\XVXTVT`@`@`@^VLZ\\XRZVXVZXXXXR\\VVZTTXT\\TZZ^TXTZVr@^d@RZT`@XTRv@f@jBrAp@Nl@`@|@n@d@Vb@XPRp@n@PFJH\\XQlDAZOfBCXMjBCLa@vDmDv[cDdYkAdLYtAKb@CN?RGl@Cj@ERu@lHEZEn@MlAIbAeDbYa@xDM`AEj@ENOhB[jAgAfJCTA^SnBc@tDi@jEm@tFFlAS~BEj@Gj@Cl@Ar@AxABh@@j@_CHi@@GJOJGFOPJ`IBb@?f@T~KA`APbKHlFr@jBd@|AmAD?j@TnLZrSDxAFjD?`@CjENFXdPFnBAf@KtN@x@JdHFdDAb@AjEx@H^vS|Al}@d@bVBzBhAfp@l@|]id@~^sb@_|@OBW`@g@f@]Xc@JyAb@CdEb@vCbEvCu@lGa@nDcK{FgOyAm@gBuASyAQoBUW?{@BKOKGUCQD[CWMeBs@cDaXHUDEJKRCNE\\AXBLCJMTE\\GRC^KXIZK^I`@Gl@CZI\\I^KVC^K\\A^O~BZBWTo@f@aAR]j@iAr@eBl@aBd@oAb@_Ah@gATg@_AoBsAoCMSGa@SKQ?MHEJ@VBTT^L`@D^ENYZe@f@o@h@]\\W^U^ELGPOXERI^EXC^Ib@KXI^ONQZUZ]^S\\[\\e@X_@XYX]N[L_A?SEa@Eo@Ia@Ee@Ge@Ia@Cg@Ak@Gi@O_@M[WKYOQCSOU_@][YOYYa@UUQ]EWGUGc@UW_@a@U]Yg@Q[IQSg@W[W_@UYI]K_@@]C_@D[Je@Fe@_B{Dy@iBqAgDSBOOYM]Mg@UYQYOSMOKOUYS]UQS]MOCa@MQCQEO?S?O?O@OASEO]AYKSIUOWA[BQEMBQEQGUEWE[EWIg@OYCSIUGUK_@M[UMOGKCMEKCKMAOCQKEOCS?UDSAKIKKIOKIOEOAOGKOAMGSQQO?M@MNKP[MUKQMOAOCS?YBM?KDMCO?UCYC_@K[I[G[Qa@WUk@Wk@I_@BY?i@B]Bk@?g@Rw@uH{HWBU?]OSOQSOSQEM@]LS?OCQHWLSHOBITGL@V@LCJMVCR?V@`@G\\GXUJQZM^Ov@Cd@?\\Db@F^EJAPUFS@MUGISIQEK@IFQNWFU?M@MFMJ[TWPYNa@Fi@Ak@Ee@B]DOA]JYJa@Te@Lm@VIF_@\\QVSNO^W^Yb@[T[d@c@X]J]TCPMDCHIHMNWQIKMMAOOOCKIIMe@]YgCCIb@}@Ze@AQKWBMAWVOA_AG]aAc@}@GWJYAM[CSc@c@WqAMa@KMLKd@QJQBa@VQr@M|@Bj@ATIPJFHNIXSVQ@IO]a@QIUo@KYBq@Ee@@Mm@c@I]KFARIHKQGKAKPe@"
        ]
      }
    ]
    
