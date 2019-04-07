'''
This rule type allows for the creation of rules which can take arbitrary sequences of commands from another rule. They are declared without extras and added in the nested property of a merge rule, the merged form of which will be used to form the extras list in ccrmerger._create_repeat_rule.

The specifications in the rule's mapping must include <sequence1> and <sequence2>, <before> and <after> are optional and allow for other commands to be spoken before or after the rule.
Example command:
"[<before>] integral from <sequence1> to <sequence2>":
            [Text("\\int _"), Key("right, caret"), Key("right")],

Any commands which come before will be executed first, then the first action in the list, then the first sequence, then the second action in the list, then the second sequence, then the final action.  At the moment sequences have a maximum length of 6 commands and before and after 8.
'''

from dragonfly import MappingRule

class NestedRule(MappingRule):
    def _process_recognition(self, value, extras):
        if "before" in extras:
            for action in extras["before"]: action.execute()
        value[0].execute()
        for action in extras["sequence1"]: action.execute()
        value[1].execute()
        for action in extras["sequence2"]: action.execute()
        value[2].execute()
        if "after" in extras:
            for action in extras["after"]: action.execute()