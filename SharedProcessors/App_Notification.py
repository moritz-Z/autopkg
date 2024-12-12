#!/usr/local/autopkg/python
#
# Copyright 2019 Greg Neagle
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
"""Processor that outputs a perosonal notification message."""


import os

from autopkglib import Processor

__all__ = ["App_Notification"]


class App_Notification(Processor):
    """This processor outputs a personal Notification."""

    input_variables = {
        "personal_message": {
            "required": False,
            "description": "Info message to output.",
            "default": "",
        }
    }
    output_variables = {
        "deprecation_summary_result": {
            "description": "Description of interesting results."
        }
    }
    description = __doc__

    def main(self):
        personal_message = self.env.get(
            "personal_message",
            "### This recipe has a personal notification. ###",
        )
        self.output(personal_message)
        #recipe_name = os.path.basename(self.env["RECIPE_PATH"])
        recipe_name = self.env.get('NAME')
        recipe_version = self.env.get('version')
        self.env["deprecation_summary_result"] = {
            "summary_text": "The following recipes have a personal notification:",
            "report_fields": ["name", "version", "information"],
            "data": {"name": recipe_name, "version": recipe_version, "information": personal_message},
        }


if __name__ == "__main__":
    PROCESSOR = App_Notification()
    PROCESSOR.execute_shell()
