#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

dwn_link = 'https://class.coursera.org/textanalytics-001/lecture/download.mp4?lecture_id=73'
file_name = 'trial_video.mp4'
urllib.request.urlretrieve(dwn_link, file_name)
