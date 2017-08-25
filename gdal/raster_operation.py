from osgeo import gdal
import osr
import numpy as np

def get_pixel_pos(lon, lat, E, N,  wres, hres):
    x = int(lon - E) / wres
    y = int(lat - N) / hres
    return int(x), int(y)

def create_geotransform(origin_lon, origin_lat, res):
   return (origin_lon, res, 0.0, origin_lat, 0.0, -res)


def epsg_to_wkt(epsg_code = 4326):
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(epsg_code)
    return srs.ExportToWkt()

def create_elevation_from_picture(pic_path, out_path, lon, lat, res):

    p = gdal.Open(pic_path)
    p_band = p.GetRasterBand(1)
    p_array = p_band.ReadAsArray()
    p_x_size = p.RasterXSize
    p_y_size = p.RasterYSize

    driver = gdal.GetDriverByName('HFA')
    driver.Register()

    out = driver.Create(out_path, p_x_size, p_y_size, 1, gdal.GDT_Float32)
    out_array = np.ones((p_y_size, p_x_size))
    out_array[p_array > 200] = 0
    out_array = out_array * 3000.0

    out.SetGeoTransform(create_geotransform(lon, lat, res))
    out.SetProjection(epsg_to_wkt(4326))

    out_band = out.GetRasterBand(1)
    out_band.WriteArray(out_array)
    out_band.FlushCache()

    geo_trans = out.GetGeoTransform()
    E = geo_trans[0]
    N = geo_trans[3]
    W = E + geo_trans[1] * p_x_size
    S = N + geo_trans[5] * p_y_size
    return E, N, W, S




# only for one band
def extent_clip(src_path, dst_path, N, S, E, W):
    ds = gdal.Open(src_path)
    driver = ds.GetDriver()

    count = ds.RasterCount
    band = ds.GetRasterBand(1)
    arr = band.ReadAsArray()
    cols = ds.RasterXSize
    rows = ds.RasterYSize
    prj = ds.GetProjection()

    geotransform = ds.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]

    ngt = (E, geotransform[1],geotransform[2],N,geotransform[4],geotransform[5])
    ltx, lty = get_pixel_pos(E, N, originX, originY, pixelWidth, pixelHeight)
    rbx, rby = get_pixel_pos(W, S, originX, originY, pixelWidth, pixelHeight)

    xSize = int(rbx - ltx)
    ySize = int(-(lty - rby))

    out = driver.Create(dst_path, xSize, ySize, 1, gdal.GDT_Float32)
    out.SetGeoTransform(ngt)
    na = np.zeros((ySize, xSize))

    for x in range(ltx, rbx):
        nx = x - ltx
        for y in range(lty, rby):
            ny = y - lty
            na[ny][nx] = arr[y][x]

    outband = out.GetRasterBand(1)
    outband.WriteArray(na, 0, 0)
    out.SetProjection(prj)
    outband.FlushCache()

if __name__ == '__main__':
    nSet = 10
    sSet = -10
    eSet = -10
    wSet = 10

    #extent_clip('world-dem.tif', 'test-dem.tif', nSet, sSet, eSet, wSet)
    e,n,w,s = create_elevation_from_picture("../data/icon.png", "../data/icon.img", 1, 0, 0.000083333333)
    print(e, n, w, s)



