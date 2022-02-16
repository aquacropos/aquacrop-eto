
import pandas as pd
from aquacropeto import *
from pathlib import Path


THIS_DIR = Path(__file__).parent

file = THIS_DIR / 'CP.dat'
order=["year","jday","maxTemp","minTemp","precip","rad"]
latitude = 40.4
elevation = 1072

def calc_faopm(file,order):
    df = pd.read_csv(file,delim_whitespace=True,header=None)
    df.columns=order
    df['date'] = pd.to_datetime(df.year, format='%Y') + pd.to_timedelta(df.jday - 1, unit='d')


    net_sw = net_in_sol_rad(df.rad)
    ext_rad = et_rad(deg2rad(latitude),sol_dec(df.jday),sunset_hour_angle(deg2rad(latitude),sol_dec(df.jday)),inv_rel_dist_earth_sun(df.jday))
    cl_sky_rad = cs_rad(elevation,ext_rad)
    net_lw_rad = net_out_lw_rad(df.minTemp,df.maxTemp,df.rad,cl_sky_rad,avp_from_tmin(df.minTemp))
    net_radiation = net_rad(net_sw,net_lw_rad)

    av_temp=(df.minTemp+df.maxTemp)*0.5

    ws=2
    svp = mean_svp(df.minTemp,df.maxTemp)
    avp = avp_from_tmin(df.minTemp)
    delta = delta_svp(av_temp)
    psy=psy_const(atm_pressure(1072))
    faopm = fao56_penman_monteith(net_radiation,av_temp+273,ws,svp,avp,delta,psy)

    df["eto"] = faopm
    df.eto=df.eto.clip(0.1)
    df=df[["minTemp","maxTemp","precip","eto",'date']]
    df.columns=["MinTemp","MaxTemp","Precipitation","ReferenceET","Date"]
    
    return df
champion_ref = pd.read_csv(THIS_DIR / 'champion_climate.txt',delim_whitespace=True, header=0)
champion_ref.columns = str("Day Month Year MinTemp MaxTemp Precipitation ReferenceET").split()

calc_from_lars = calc_faopm(file,order)

print(champion_ref["MinTemp MaxTemp Precipitation ReferenceET".split()].mean())
print(calc_from_lars["MinTemp MaxTemp Precipitation ReferenceET".split()].mean())