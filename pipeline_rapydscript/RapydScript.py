from __future__ import unicode_literals

from conf import settings as settings
from pipeline.compilers import SubProcessCompiler


class RapydScriptCompiler(SubProcessCompiler):
    output_extension = 'js'

    def match_file(self, path):
        return path.endswith('.rapydscript') or path.endswith('.pyj')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return  # File doesn't need to be recompiled
        command = "%s %s %s > %s" % (
            settings.PIPELINE_RAPYD_SCRIPT_BINARY,
            infile,
            settings.PIPELINE_RAPYD_SCRIPT_ARGUMENTS,
            outfile
        )
        return self.execute_command(command)
