### Shared Processors

- App_Notification
- StopProcessingIf_Notification

## App_Notification

Here's an example of using App_Notification

```
<dict>
    <key>Arguments</key>
    <dict>
      <key>personal_message</key>
      <string>This is your message to output</string>
    </dict>
    <key>Processor</key>
    <string>com.github.moritz-Z.SharedProcessors/App_Notification</string>
</dict>
```

## StopProcessingIf_Notification

Here's an example of using StopProcessingIf_Notification.
This Processor combinates the default StopProcessingIf with the option to display an individual mesage.
If 'StopProcessingIf' condition applies, AutoPackager stop processing a recipe.

```
<dict>
    <key>Arguments</key>
    <dict>
        <key>personal_message</key>
        <string>Only if condition is true, this message will be displayed.</string>
        <key>predicate</key>
        <string>Condition equivals True</string>
    </dict>
    <key>Processor</key>
    <string>com.github.moritz-Z.SharedProcessors/StopProcessingIf_Notification</string>
</dict>
```


`e.g. Output if JamfPatchChecker does not find a matching version for Google Chrome Version '132.0.6834.80'`
```
- Verbose Log:

JamfPatchChecker: WARNING: Could not find matching version '132.0.6834.80' in patch softwaretitle 'Google Chrome'.
Latest reported version is '132.0.6834.84'.
{'Output': {'jamfpatchchecker_summary_result':
    {'data': {'     latest_version_found': '132.0.6834.84',
                    'package_version': '132.0.6834.80',
                    'patch_softwaretitle': 'Google Chrome',
                    'patch_softwaretitle_id': '94'},
    'report_fields':    ['patch_softwaretitle_id',
                        'patch_softwaretitle',
                        'package_version',
                        'latest_version_found'],
    'summary_text': 'The following patch policies were checked in Jamf Pro:'}}}

com.github.moritz-Z.SharedProcessors/StopProcessingIf_Notification
{'Input': {'personal_message': 'Personal Message for output to the user',
          'predicate': 'patch_version_found != True'}}
StopProcessingIf_Notification: (patch_version_found != True) is True
StopProcessingIf_Notification: Personal Message for output to the user
{'Output': {'deprecation_summary_result': {'data': {'information': 'Personal Message for output to the user',
                                                    'name': 'Google Chrome',
                                                    'version': '132.0.6834.80'},
                                           'report_fields': ['name',
                                                             'version',
                                                             'information'],
                                           'summary_text': 'The following recipes were stoppt by an condition and may have a personal notification:'},
            'stop_processing_recipe': True}}


- summary recipe

The following patch policies were checked in Jamf Pro:
    Patch Softwaretitle Id  Patch Softwaretitle  Package Version  Latest Version Found  
    ----------------------  -------------------  ---------------  --------------------  
    94                      Google Chrome        132.0.6834.80    132.0.6834.84         

The following recipes were stoppt by an condition and may have a personal notification:
    Name           Version        Information                                                                                                                                           
    ----           -------        -----------                                                                                                                                           
    Google Chrome  132.0.6834.80  PPersonal Message for output to the user
```
