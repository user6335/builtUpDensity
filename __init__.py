# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BuiltUpDensitiy
                                 A QGIS plugin
 This plugin can calculate the density of the built-up area using remote sensing raster data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-04-20
        copyright            : (C) 2021 by Farid Azhari, Fatwa Ramdani, Bondan Sapta Prakoso (Geoinformatics Research Group Brawijaya University)
        email                : user6335@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BuiltUpDensitiy class from file BuiltUpDensitiy.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .BuiltUpDensitiy import BuiltUpDensitiy
    return BuiltUpDensitiy(iface)
