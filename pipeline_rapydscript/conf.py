# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings as _settings
from pipeline.conf import DEFAULTS, PipelineSettings

DEFAULTS=DEFAULTS.update(
  {
    'PIPELINE_RAPYD_SCRIPT_BINARY': '/usr/bin/env rapydscript',
    'PIPELINE_RAPYD_SCRIPT_ARGUMENTS': '',
  }
)

settings = PipelineSettings(_settings)
