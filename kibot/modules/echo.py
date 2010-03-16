import kibot.BaseModule

class echo(kibot.BaseModule.BaseModule):
    _cperm = 1
    def __call__(self, cmd):
        """Echo echo echo."""
        cmd.nreply(cmd.args)
