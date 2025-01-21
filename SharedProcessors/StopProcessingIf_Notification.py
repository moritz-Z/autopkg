#!/usr/local/autopkg/python
#
# Copyright 2013 Greg Neagle
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for StopProcessingIf class"""

from autopkglib import Processor, ProcessorError, log

try:
    from Foundation import NSPredicate
except ImportError:
    log("WARNING: Failed 'from Foundation import NSPredicate' in " + __name__)

__all__ = ["StopProcessingIf_Notification"]


class StopProcessingIf_Notification(Processor):
    """Sets a variable to tell AutoPackager to stop processing a recipe if a
    predicate comparison evaluates to true."""

    description = __doc__
    input_variables = {
        "predicate": {
            "required": True,
            "description": (
                "NSPredicate-style comparison against an environment key. See "
                "http://developer.apple.com/library/mac/#documentation/"
                "Cocoa/Conceptual/Predicates/Articles/pSyntax.html"
            ),
        },
        "personal_message": {
            "required": False,
            "description": "Info message to output.",
            "default": "",
        }
    }
    output_variables = {
        "stop_processing_recipe": {
            "description": "Boolean. Should we stop processing the recipe?"
        },
        "deprecation_summary_result": {
            "description": "Description of interesting results."
        }
    }

    def predicate_evaluates_as_true(self, predicate_string):
        """Evaluates predicate against our environment dictionary"""
        try:
            predicate = NSPredicate.predicateWithFormat_(predicate_string)
        except Exception as err:
            raise ProcessorError(
                f"Predicate error for '{predicate_string}': {err}"
            ) from err

        result = predicate.evaluateWithObject_(self.env)
        self.output(f"({predicate_string}) is {result}")
        return result

    def main(self):
        self.env["stop_processing_recipe"] = self.predicate_evaluates_as_true(
            self.env["predicate"]
        )
        if self.env["stop_processing_recipe"]:
                    personal_message = self.env.get(
                        "personal_message",
                        "### This recipe has a personal notification. ###",
                    )
                    self.output(personal_message)
                    #recipe_name = os.path.basename(self.env["RECIPE_PATH"])
                    recipe_name = self.env.get('NAME')
                    recipe_version = self.env.get('version')
                    self.env["deprecation_summary_result"] = {
                        "summary_text": "The following recipes were stoppt by an condition and may have a personal notification:",
                        "report_fields": ["name", "version", "information"],
                        "data": {"name": recipe_name, "version": recipe_version, "information": personal_message},
                    }


if __name__ == "__main__":
    PROCESSOR = StopProcessingIf_Notification()
    PROCESSOR.execute_shell()
