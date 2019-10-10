def before_scenario(context, scenario):
    print("Before scenario")
    context.parm1 = context.config.userdata.get("parm1", "parm1_1")
    context.parm2 = context.config.userdata.get("parm2", "parm2_1")
    context.parm3 = context.config.userdata.get("parm3", "parm3_1")


def after_scenario(context, scenario):
    print("After scenario")
