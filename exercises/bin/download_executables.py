import sys
import pymake

def get_platform(pltfrm):
    # Determine the platform in order to construct the zip file name
    if pltfrm is None:
        if sys.platform.lower() == 'darwin':
            pltfrm = 'mac'
        elif sys.platform.lower().startswith('linux'):
            pltfrm = 'linux'
        elif 'win' in sys.platform.lower():
            is_64bits = sys.maxsize > 2 ** 32
            if is_64bits:
                pltfrm = 'win64'
            else:
                pltfrm = 'win32'
        else:
            errmsg = ('Could not determine platform'
                      '.  sys.platform is {}'.format(sys.platform))
            raise Exception(errmsg)
    else:
        assert pltfrm in ['mac', 'linux', 'win32', 'win64']
    return pltfrm


def getmfexes(pth='.', version='', pltfrm=None):
    """
    Get the latest MODFLOW binary executables from a github site
    (https://github.com/MODFLOW-USGS/executables) for the specified
    operating system and put them in the specified path.

    Parameters
    ----------
    pth : str
        Location to put the executables (default is current working directory)

    version : str
        Version of the MODFLOW-USGS/executables release to use.

    pltfrm : str
        Platform that will run the executables.  Valid values include mac,
        linux, win32 and win64.  If platform is None, then routine will
        download the latest appropriate zipfile from the github repository
        based on the platform running this script.

    """

    # Determine the platform in order to construct the zip file name
    pltfrm = get_platform(pltfrm)
    zipname = '{}.zip'.format(pltfrm)

    # Determine path for file download and then download and unzip
    url = ('https://github.com/MODFLOW-USGS/executables/'
           'releases/download/{}/'.format(version))
    assets = {p: url + p for p in ['mac.zip', 'linux.zip',
                                   'win32.zip', 'win64.zip']}
    download_url = assets[zipname]
    pymake.download_and_unzip(download_url, pth)

    return


if __name__ == "__main__":
    pltfrm = get_platform(None)
    getmfexes(version='2.0', pth=pltfrm)
