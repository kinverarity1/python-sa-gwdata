Natural resource management (NRM) region
========================================

`GetNRMRegionSearchData?NRMRegion=Kangaroo Island <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDDMS.ashx/GetNRMRegionSearchData?NRMRegion=Kangaroo Island>`__

The :ref:`webservice-metadata` section shows how to retrieve the NRM names which can be used in this request.

Returns groundwater data (this only shows 2 of many returned "DHNO" records):

.. code-block:: json

    [
    {
        "DHNO": 16905,
        "LAT": -36.0446216,
        "LON": 136.7494448,
        "MAPNUM": 622500001,
        "PURP_DESC": "SPR",
        "SWL": 0,
        "TDS": 1564,
        "CLASS": "WP",
        "NRM": "Kangaroo Island",
        "LOGDRILL": "N",
        "LITHOLOG": "N",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "1983-12-21",
        "LATEST_SAL_DATE": "1983-12-21"
    },
    {
        "NAME": "CR 2B",
        "DHNO": 227963,
        "LAT": -35.7756614,
        "LON": 138.0033454,
        "MAPNUM": 652600563,
        "MAX_DEPTH": 6,
        "OBSNUMBER": "DUD016",
        "PURP_DESC": "INV",
        "SWL": -0.44,
        "TDS": 5445,
        "CLASS": "WW",
        "NRM": "Kangaroo Island",
        "LOGDRILL": "N",
        "LITHOLOG": "Y",
        "CHEM": "N",
        "WATER": "Y",
        "SAL": "Y",
        "OBSWELL": "N",
        "STRATLOG": "N",
        "HSTRATLOG": "N",
        "LATEST_SWL_DATE": "2009-02-23",
        "LATEST_SAL_DATE": "2006-09-06",
        "LATEST_OPEN_DEPTH": 6,
        "LATEST_OPEN_DATE": "2006-05-16"
    }
    ]

There is also the related query `GetNRMRegionFromName?NAME=Kangaroo Island <https://www.waterconnect.sa.gov.au/_layouts/15/dfw.sharepoint.wdd/WDDWFS.ashx/GetNRMRegionFromName?NAME=Kangaroo Island>`__

.. include:: polyline-explainer.rst

Returns:

.. code-block:: json

    [
    {
        "OBJECTID": 6,
        "REGION_ID": 4,
        "NAME": "Kangaroo Island",
        "OFFICE_ID": 24,
        "SHAPE.AREA": 10535165522.761,
        "SHAPE.LEN": 585550.95053677,
        "URL": "http:\/\/sdsi.sa.gov.au\/arcgis\/rest\/services\/DEWNRint\/WaterConnect_WaterConnect\/MapServer\/",
        "Boundary": [
        "d`|vEq}pfY|EgnB?KzEm`B`Fc`B?K|Se|B?o`B?cjC?KsyAmgl@|EudAzSuo@vTs_@bSc]to@uh@tdAya@dd\\skAvh@_Ft}@{Lrv@{h@ljH{vEvv@uo@l[gXfa@o]f]e]lXoXvv@sv@to@w}@|a@wv@th@s}@xo@qrAxdFgmIxZyo@|Lwh@zSuv@zSu}@|SsrAzSo`B~EgcCzEgqC{EsyA?qdA_FudA~EorAzEu}@~Ew}@zSsv@zh@yv@rv@sv@t}@w}@heAaw@zw@ml@Z[lIhEnFzBlF`ChFhCbGpBtHpCnH~CtHjDpHxDjHdEfHpE~G|ExGhFrGvFhH`G`HpGvGzGpGhHfGtH|F`IrFjIjFvI~E`JtEhJhEtJ~D|JrDbKfDlKzCtKnCzKvvB`xHtvBdxHnfBjnG~EvJrE`KhEhKzDrKnDzKnDxJdDbKzCfKlCnKbCtKvBzKjB~K~AbLtAlLhAnLhG|G`GfHxFrHnF~HfFfIzErIrEzIjGrGbG|GzFhHpFtHjF~H~EfIlFdIbFnIxEvIT^p@^nIvEhIfF`IvFxHdGpHrGhHbH~GnHvEpFrExFtEfGnEpGfEvGdEvG~D|GvDdHnDjHhCvFpBzC~EhHxEpHpEzHfEbI~DjI~@fBxEdJnEnJdEvJxD~JxDjKjDpK`DxKpCvKdC~KxBdLlBhL~AlLrArLfAtLx@xLl@zL^zLP~LD|LG~LU|L[bLi@bLw@xLcAtLoArL}AnLBnMInMYnMe@lMu@jMaAfMgAbLsA`L_B|KiBxKuBrKgBrIwBnKeCjKmCbKyC|JeDvJeC~GkCxG}BfGyCxIaDrIGPmCpIuClI}CdI}DlJgEdJsE|I{ErIw@jKcAfKkAfKaBrLmBpLyBhLeCdLsC~K_DvKmDpKwDfKcE~JiChGqCdGoEdJyEzIeFpImFfIwEvG_FnGeFfGmF~FqFtF}@jDcBxJmBrJwBpJaCjJiCdJQvBfBfH`BjH~CpJtCzJjC~J`CdKtBhKhBnK~ArKtAvKfAzK|@|K~@hKr@jKh@jK^nKRnKJnK?pKZdMLdM@dMMdMYdMg@bMs@`McA~LoAzL}AvL_BzKkBvKwBrKcCjKmCfKyC`KcDzJiDjJsDdJ}D|IgEtIqEjIyEbIaFzHmD`GsDzFEnBOtK[vKg@tKo@xKy@vKcAtKcAdJmAbJuA~I}AzIYlCl@nKb@nKXpKLrKBrKErKQpKHhMCfMOfM_@fM[vHa@vHg@vHlFrEjFzEhGnFbGzFzFbGtFnGlFvGfFbH|EhHdFdI|ElIjEdI`EjIxDtInDzIdDbJ|ChJpCpJtCtKjC~K|BbLpBfLvA`JnAbJdAdJ|@zIt@zIj@|Id@~IXzFf@hMXjMJjMCjMOjM]hMk@hMe@tHk@tHPnHLnHd@`H\\bHr@|Ih@~IpAdLdAjLx@lLNrAjB~J~AbKtAfKhAhKfAjH~@nHp@hFl@jFjA`EfCbH|D~HtDdIlDnItDzJjDdKxDjIjD~GdDbHdGuGjGiGtG}FxGqF`HgFfHyElHkErHaExHqDhFkDjFaD|FcD`G{CbGqCzHkD`I}CbIoChIaCrIyBxIiBxIyA|IkA~I{@`Jm@`J]`JMbJ@`JN`J^lJn@jJ~@hJpAdJ~AbJpB~I~B|IpCtI~CvIpBtI~BnInCjI|CfIjD`IxD|HhEtHtEnHbFlIdCfIpCbI`D~HlDxH|DjIpEbI`FzHnFtH~FjHjGdHzGhDlDhDrDnGnHfGzH|FfIrFrIfF|I~EfJxGpGpG~GfGhH~FtHtF`IlFjIbFtIvE`JnEfJbErJxDxJb@lAnGnHdGzHzFdIrFrIfF|I|EfJrEnJfEzJzDbKnDjKdDrKvCxKfCfKzBnKnBpKdBvKvAzKlA~K`A`Lv@dLh@fL\\fLRhLjArJbAvJx@xJp@zJd@zJ`@tF^vFfAxK|@|Kp@`Ld@`LZbLXh@fCfDbHnF~G|FtGjG|AxAzAiLfBeLtB_L~ByKlCuKvCmKbDgKlD_KxDwJtBcFxBaFhEaJpEyI|EoIdFeInF{HvFoH~FgHhGyG`FgFfF}ElFuErGiFxG}E~GqEbHeEhIqEpIaEtIqDxIcD~IqCbJaCfJsBhJaBlJoAnJ_ApJo@pJ]pJMrJ@rJTpJb@nJt@nJfAjJvAhJfBdJvB`JhC|IvCxIhDrIvDlIfEdIvE`IdFxHrFpHbGhHnG`H|GxGjHnGvHdGbIzFnIpFzIfFdJzEnJpExJbEnJvDtJjD~J`DdKrC|JfC`K|BhKfB~I~A`JtAfJvAjKjAnK~@rKz@pLn@rL`@tLTvLFpHBpHGhMShMa@hMm@fM}@bMkA`MwA|LeBxLsBtL_ClLkChLyC`LgDxKqDrK}DhKkE~JuEvJ_FlJmFjJyF`JcGrImGhIwGzHaHlHiH~GaHdGgHvFoHhFuH|E{HlEaI`EgIpDkIbDqItCyIjC_JzBaJjBeJ|AgJjAiJz@kJj@kJXkJJmJEkJUkJe@hDvK~C~KpCfLbClLxBpLhBxL|AzLnA`M`AbMr@fMf@fMVxLLxL?xLKzLYvLe@vLs@tL_ArLkAnLyAjLcBhLqBbL}B|KiCvKuCpKaDjKkDbK{DhKgE~JsEtJ}ElJiF`JsFvI}FlIgG~HqGrHyGfHcHxGiHlGsH|F{HpF_I`FiIrEmIbEsItDyIdD}ItCaJbCeJtBiJbBcCpDgClD_BbMkB|L{BvLgCpLuCjLaDbLmD|K{DrKgEhKsE`K_FvJkFjJuF`J_GtIiGhIuGzH}GnHgH`HoHrGwHdGiHjFoHzEuHnE{H`E_IrDeIfDiIvCiD`IqD|HwDrHaEnHgEdHv@dLh@dL^hLRhLpA~LdAbMv@fMf@fMZjMLjM?jMMhM[jMi@fMw@fMeAbMsA~L_BzLmBvL{BpLgCjLsBlIyBfIaCbIiC~IuCxI{CrIeDlIc@vJm@tJu@pJW|Ke@|Ko@xKy@xKeAtKqApK{AnKgBhKeBnJoBjJwBdJaC`JkC|IsBrIwBlJ_ChJiCbJqC|I{CxIcDpI|Tnw@xGrFpG`GnGlGhGxG`GdHvFpHpFzH~HfEzHtE~HfFvHvFnHbGhHrG~G~GvGlHlGxHbGdIxFpInF|IdFdJxEpJlEzJbEdKvDlKjDtK|CzKxBtInBxItClKhCrK~BvKpB~KdBbLvAjKhAlK`ApKv@zKl@|K`@~KtDtKhD|K|CdLnCjL`CpLrB`LfBdLxAhLlAlL`ApLt@rL^zHXzHRzHPtLBvLGvLStLa@tLm@rL{@nLeAnLkAjKuAfK_BbKkB~JsBzJ_CvJgCpJ{B~JeCzJoCrJ{BnHcChHiCbH?jMMhM[fMi@fMq@hL{@hLiAdLuA`L_B|KtC|KhCdL|BjLnBpLbBtLtAxLhAzLx@`Mn@`M^dMPdMDdMAdHGfHAfA\\rJRrJJrJ@tJCfLMfLYfLg@dLq@bL}@~Ki@vKs@rK_AnKiAnKuAjK_BfKmBzL{BvLgCpLuChLcDbLmDxKRhFPhFz@vFv@xFD\\vCzJjCbK`CfKnBrJfBvJzA|JpA~JhAbK`AvJv@xJl@zJb@|JtBfLP`AhFbJ|EjJrEtJfE~JzDhKnDnKfD|KzCbLlCjLxCxIpC|IhCdJ|BfJtBnJjBpJvArHpAvHRlA`B~JvA`KhAtJ`AvJjA`M|@fMn@fM`@jMPjMDjMCzJKxJIfHMdHAjJKjJSjJ[jJm@dMy@bMgA~LuA|LcBxLoBrL{BlLiChLdDlJ|CvJpCzJfCbK|BfKpBlKpBnLbBtLtAxLhAzLz@~Ln@bM^bMRdMDdMEdMUdMa@bMo@`M}@~LiA|LwAvLcBtLsBnL}BhLkCbLwC|KcDtKoDnK{DdK@fAJxFDzFBtLGtLStLa@rLm@pLy@pLlB|FjB~FxA~EtA~EpCbGrDnIhDvI~CzIvCbJlChJbCnJzBrJ~BhLpBlLdBrLxAtLhAzL~@|Ln@`Mb@`MTdMFbMXtLJtL?tLbJbC~IrCzIbDtIrDpI`EhIpEbI`F|HnFrH~FlHjGdHxGzGfHrGrHhG~H~FlItFvIjF`J~ElJtEvJjE`K`EfKtDrKfDxKzC`LnCfL`CnLtBrLfBxLxA|LlA`M~@dMn@vKb@vKXxKLxJDzJ@~GEhMShMa@hMm@fM}@bMcAlLqAjL}AdLiB`LuB|K_CvKmCpKuCjKcDdKmD|JyDtJgE|JsEtJ}ElJiF`JsFtI_GjIaFvGgFnGoFfGwFzF{FpFcGhFwGlF_H`F_IjFgI|EmIlEqIpEwI`E}IpDaJ`DgJpCkJ~BoJnBsJ|AsJjAwJz@yJh@qJXsJFsJGqJWqJi@qJ{@mJiA}HkA}HwAyHeBwHoBsH}B}FoBsJ`BuJnAwJ|@yJl@yJX{JH{JGyJYyJk@yJ{@uJmAqJ_BqJqBkJaCgJsCcJcDeI~DkIpDqI`DuF~H}FrHgGhHqGzGwGpG_HbGeHvFkHjFsH|EyHnE_IbEsGxH_HlHgH~GdApJz@rJr@tJh@vJ^xJPjFLjFNxHFzHBxHEnLQnL[lLi@lLw@hLaAhLmAbLyA`LkBvLyBpLmB~K{BxKeCrKqClK}CfKgD`KsDvJ}DpJgEfJsE~I}EtIeFjIoF`IyFtHsDhKaE`KkEvJwEnJaFdJkFxIwFnI_GbI{FnHeGbHkGxGuGjG{G`GsGfFyG~E_HpEcHdEgHzDmHnDoHbDuHtCyHhC}HzBiJ~BmJlBqJ|AsJjAuJz@uJh@yJVwJDkA`JsA~IoBjL}BdLkC~KuCxKaDrKoDhKyDbKeExJoEpJ{EfJeF|IoFpIyFfIcG|HmGnHuGbH}GvGgHhGiH|FqHlFyH`F_IrEeIbEiItDoIfDuIvCyIfCcJ|BiJlBkJzAoJjAoJz@qJh@sJXaIJuzErwEuzElwEwzEfwEy~Ad}AqYbYqjKilCaqH_vBgmGecBkPwFqEwCkJcFuLsHqNiPsmZ}zZwEwEgC_CcF_E{CuByE}CKC~xForc@|Lk`B`FmyA}EkkA?K}EguB{SkuBsrAifImbTetxA}SorA?skACojCua@otX?ecC?K|EiyA",
        "vym}EsntdYTnMDpMEpMUnMa@lMo@lM_AhMkAfMyA`MgB~LsBvLcCrLmClL}CdLgD~KuDtKaElKmEdKyExJeFpJmFbJ{FzIcGlIoG`IwGrHaHfHiHzGqHjG{H|FaIlFgI~EoInEuI`E{InD_J~CeJnCgJ~BmJlBoJ|AqJjAsJz@uJh@wJVwJDmJEkJWmJg@iJy@iJgAgJyAcJiB_JwBuGiBsGsBqG}BqIgDmIuDgIeEaIsE{HaFuHqFkH}FeHkG}GyGuGcHkGqHaG{HyFcIoFqIcFyI{EeJoEmJeEwJ{D_KmDgKcDoKwCwKeHaEaHoEyG{EuGeFmGqFuGoEmF`GqFxFyFlF}FdFaHrFgHfFkHzEsHjEyH~D}HrDcIbDgItCeIfCiIxBmIhBoI|AqInAsI~@uIp@uIb@wIRwIDuJGsJWsJk@qJy@mJkAmJ}AiJmBgJ}BaJoC}I_DwImDsI_EmImEeI}EaIkFwHyFoHiGiHwG_HcHuGqHmG}HcGiIyFuIoFaJcFkJyEuJmE_KaEiKuDeKgDmK}CuKqC{KcCcLyBgLkBmL}AqLsAuLcAyLy@{Li@_M_@_MOaMEoMFqMToMb@oMr@kM~@iMlAgMzAcMhB}LvByLbCqLpCmL~CeL~CgKhD_KtDwJ~DoJjEgJrE}I~EuIfFkIpF_IbGcIlGwHtGiH|G_HfHoGlHcGvHuF|HeFbIyEhIiEnIyDtIkDzIyC|IkCbJ{BdJkBhJyAjJkAlJy@lJg@nJYpJExJDxJXvJh@vJ|@rJlArJ|AlJnBjJ`CfJpC`JbD|IrDtI`EpIrEhIbFbIpFnFcGrF{FzFqF`GeFfG}EtHqFzHcF`IuEfIgEnIwDpIiDxIwCzIiC~IyBbJiBfJyAfJiAjJy@jJg@lJWlJGhIDhIPhI`@fIl@dIx@dIhA`ItA`JjB~IzBxIjCtIzCpIhDjIxDfIhEhIdDdItD~HbEfIvE`IfFxHvFpHbGjHrG`H~GvGlHnGxHfGdIzFpIpF|IfFhJzEpJnE|JdEdKxDnKlDvK~C|KtCdLvHvEpHdFhHpFbH~FzGjGrGvGjGdHbGnHxFzHnFdIpFzIdFdJxEpJfEbJzDlJpDrJfD|J|C`KpChKdCnKzBtKnBzKzAjJrAnJxAbMjAfM~@hMn@lM`@nM",
        "b}~{EwzdbYRlMDnMEpMSrMc@pMo@nM_AjMmAhM{AdMgB`MsBrL_CjLmCfLyC`LeDxKqDnK_EhKiE~JuEvJ_FjJkF`JuFvI_GhIiG~HqGrH}GdHcHxGmHjGsHzF}HnFcI~EiIpEoIbEuIpDwIbD_JrCaJdCeJrBiJbBkJpAoJ`AoJp@qJ^qJNqJ?qJQqJc@oJq@_J}@{ImAyI{AwIkBsIyBoIgCmIwCgIeDaIsD}HaEwHoEqH}EyHuFsHcGoHqGgHaH}GoHsG{HkGgI_GuIuF_JkFkJ_FuJsEaKgEiK{DqKoD{KaDcLuCiLiCqLyAyHsA}HmA}H{AmLoAoLcAsLw@wLi@wL]yLO{LEyLF{LRwL^yLl@uLx@uLdAqLrAmL~AiLjBeLxB_LbC{KnCuKzCmKfDiKpDaKzDyJfEqJrEgJ|E_JdFsIpFiIxF_IbGsHjGgHtG{G|GoGbHcGjHuFrHgFhHqEnHcEtHwDxHiD|H}CbIoCdI_ChIuBlIeBnJ_BrJqArJ}@vJm@vJ[vJKvJFxJVtJf@tJz@rJjAnJzAlJnBjJ|BtIfCrIvCnIdDhItDbIbE|HpEvH~EpHlFhHzF`HfGxGtGrG~GhGlH~FxHvFbIjFnIbFxIxE`JnElJdDvH~CzHvCbIlCfIdC~HzBdItBhIlBlI`CrLtBvLdBzLxA`MlAdM|@hMn@jM`@lM"
        ]
    }
    ]

.. include:: footer.rst