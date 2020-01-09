# python-sa-gwdata

[![License](http://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kinverarity1/aseg_gdf2/blob/master/LICENSE)

Python code to get groundwater data for South Australia

This code provides the Python package ``sa_gwdata`` to make it easier to download and access groundwater data from the South Australian Department for Environment and Water's [Groundwater Data website](https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Default.aspx). It also provides some help for getting related data from the Department for Energy and Mining's [South Australian Resources Information Gateway (SARIG) website](https://minerals.sarig.sa.gov.au/QuickSearch.aspx).

This is an unofficial side-project done in my spare time.

## How to use

Check out the [complete package documentation](https://python-sa-gwdata.readthedocs.io/en/latest/index.html), and
some tutorial Jupyter Notebooks in the [notebooks](notebooks) folder.

Define the wells you are interested in manually:

```python
>>> import sa_gwdata
>>> wells = sa_gwdata.find_wells("5928-203", "ule 96")
>>> wells
["LKW042", "ULE096"]
```

(It has recognised automatically that [5928-203](https://www.waterconnect.sa.gov.au/Systems/GD/Pages/Details.aspx?DHNO=7207&PN=1421712654109#Summary) is also known as LKW042).

Or search for wells by geographic area:

```python
>>> wells = sa_gwdata.find_wells_in_lat_lon([-34.65, -34.62], [135.47, 135.51])
```

Then you can download data as pandas DataFrames:

```python
>>> wls = sa_gwdata.water_levels(wells)
>>> tds = sa_gwdata.salinities(wells)
>>> dlogs = sa_gwdata.drillers_logs(wells)
```

There is also full access to the underlying [set of web services](https://python-sa-gwdata.readthedocs.io/en/latest/webservices.html) which provide a variety of data in JSON format.

Start a session with Groundwater Data:

```python
>>> session = sa_gwdata.WaterConnectSession()
```

On initialisation it downloads some summary information.

```python
>>> session.networks
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
>>> r = session.get("GetObswellNetworkData", params={"Network": "CENT_ADEL"})
>>> r.df.head(5)
```

```
	aq_mon	chem	class	dhno	drill_date	lat	latest_open_date	latest_open_depth	latest_sal_date	latest_swl_date	...	pwa	replaceunitnum	sal	salstatus	stat_desc	swl	swlstatus	tds	water	yield
0	Tomw(T2)	Y	WW	27382	1968-02-07	-34.764662	1992-02-20	225.00	2013-09-02	2018-09-18	...	Central Adelaide	NaN	Y	C	OPR	3.47	C	3620.0	Y	2.00
1	Qhcks	N	WW	27437	1963-01-01	-34.800905	1963-01-01	6.40	1984-02-01	1986-03-05	...	Central Adelaide	NaN	Y	H	NaN	5.86	H	1121.0	Y	NaN
2	Tomw(T1)	Y	WW	27443	1972-04-20	-34.811124	2014-04-01	0.00	1991-10-09	2003-07-04	...	Central Adelaide	NaN	Y	H	BKF	NaN	H	2030.0	Y	5.00
3	Tomw(T1)	Y	WW	27504	1978-02-28	-34.779893	1978-02-28	144.50	2016-04-06	2011-09-18	...	Central Adelaide	NaN	Y	H	OPR	11.21	H	2738.0	Y	0.00
4	Tomw(T1)	Y	WW	27569	1975-01-01	-34.891250	1975-07-09	131.10	1986-11-13	1988-09-21	...	Central Adelaide	NaN	Y	H	BKF	9.90	H	42070.0	Y	12.50
```

## Install

You will need Python 3.6 or a more recent version.

```bash
$ pip install -U python-sa-gwdata
```

This installs the latest [release](https://github.com/kinverarity1/python-sa-gwdata/releases) of the Python package ``sa_gwdata``.

To install the latest code from GitHub, make sure you the dependencies ``pandas`` and ``requests`` installed, then use:

```bash
$ pip install https://github.com/kinverarity1/python-sa-gwdata/archive/master.zip
```

## License

MIT
