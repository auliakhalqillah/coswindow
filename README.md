# COSWINDOW
This program is used to generate cosine window function through the function of
`coswindow`. The module has been written and tested in Python 3.7.
# INSTALL
1. Go to the folder where the `setup.py` file is through terminal
2. Type the following command in your terminal:
```
python3 setup.py install --record installpath.txt
```
  it will generate `installpath.txt` file as information where the library of coswin is<br>
3. Check the module of `coswin` by running file `run_coswindow.py` inside `test` folder through terminal:
```
python3 run_coswindow.py
```
it will show input parameter for the user as follows:
```
---------------
INPUT PARAMETER
---------------
Taper Ratio 		:0.5
Sampling Time 		:0.01
Signal Frequancey 	:2
```
if the module of `coswin` is successfully installed, the output figure will show up (e.g. example.png)

# USAGE
To use this function, you can type the following command:
```
from coswindow import coswin
...
...
...
output = coswin(a,n)
```
where the `a` is the bandwidth of taper and `n` is the number of sample that want to be generated
# REQUIRED
1. Numpy
2. Math
3. Matplotlib
# CREATED BY
Aulia Khalqillah,S.Si.,M.Si(2020)
Email: auliakhalqillah.mail@gmail.com
# SOURCE
Marco Pilz and Stefano Parolai,Helmholtz Centre Potsdam, GFZ <br>[Tapering of windowed time series (DOI: 10.2312/GFZ.NMSOP-2_IS_14.1)](http://gfzpublic.gfz-potsdam.de/pubman/faces/viewItemOverviewPage.jsp?itemId=escidoc:56141)
