# waterconnect

Python -> pandas wrapper for groundwater data on [WaterConnect](https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Default.aspx)

Unofficial.

## Install

```
$ pip install waterconnect
```

## How to use

Everything starts with a web session:

```python
>>> from waterconnect import groundwater
>>> s = groundwater.Session()
```

On initialisation it downloads some summary information.

```python
>>> s.networks
{'ANGBRM': 'Angas Bremer PWA',
 'AW_NP': 'Alinytjara Wilurara Non-Prescribed Area',
 'BAROOTA': 'Baroota PWRA',
 'BAROSSA': 'Barossa PWRA',
 'BAROSS_IRR': 'Barossa irrigation wells salinity monitoring',
 'BERI_REN': 'Berri and Renmark Irrigation Areas',
 'BOT_GDNS': 'Botanic Gardens wetlands',
 'CENT_ADEL': 'Central Adelaide PWA',
 'CHOWILLA': 'Chowilla Floodplain',
 ...
}
```

With this information we can make some direct REST calls:

```python
>>> r = s.get("GetObswellNetworkData", params={"Network": "CENT_ADEL"})
>>> r.df.head(5)
	aq_mon	chem	class	dhno	drill_date	lat	latest_open_date	latest_open_depth	latest_sal_date	latest_swl_date	...	pwa	replaceunitnum	sal	salstatus	stat_desc	swl	swlstatus	tds	water	yield
0	Tomw(T2)	Y	WW	27382	1968-02-07	-34.764662	1992-02-20	225.00	2013-09-02	2018-09-18	...	Central Adelaide	NaN	Y	C	OPR	3.47	C	3620.0	Y	2.00
1	Qhcks	N	WW	27437	1963-01-01	-34.800905	1963-01-01	6.40	1984-02-01	1986-03-05	...	Central Adelaide	NaN	Y	H	NaN	5.86	H	1121.0	Y	NaN
2	Tomw(T1)	Y	WW	27443	1972-04-20	-34.811124	2014-04-01	0.00	1991-10-09	2003-07-04	...	Central Adelaide	NaN	Y	H	BKF	NaN	H	2030.0	Y	5.00
3	Tomw(T1)	Y	WW	27504	1978-02-28	-34.779893	1978-02-28	144.50	2016-04-06	2011-09-18	...	Central Adelaide	NaN	Y	H	OPR	11.21	H	2738.0	Y	0.00
4	Tomw(T1)	Y	WW	27569	1975-01-01	-34.891250	1975-07-09	131.10	1986-11-13	1988-09-21	...	Central Adelaide	NaN	Y	H	BKF	9.90	H	42070.0	Y	12.50
```

Get water levels:

```python
>>> wl = s.get("GetWaterLevelDetails", params={"DHNO": 188444}).df
>>> wl.head(5)
	anomalous_ind	data_source_code	measured_during	obs_date	pumping_ind	rswl	standing_water_level
0	N	DEWNR	D	2002-01-28	N	-8.12	15.08
1	N	DEWNR	M	2002-03-06	N	-12.50	19.46
2	N	DEWNR	M	2002-10-02	N	-3.43	10.39
3	N	DEWNR	M	2003-03-04	N	-11.69	18.65
4	N	DEWNR	M	2003-09-27	N	-1.93	8.89
```
