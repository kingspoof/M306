from Modules.DataInput import DataInput
from Modules.DataProcessing import DataProcessing
from Modules.DataOutput import DataOutput

from Datamodels.DataObject import DataObject


model_DataInput = DataInput()
model_DataProcessing = DataProcessing()
model_DataOutput = DataOutput()


dataObject = DataObject()

print('------------- Begin reading ...')
height, widht, all_words, spezial_words = model_DataInput.process()
print('------------- Begin Processing ...')
field_words, field_words_caps, field = model_DataProcessing.process(height, widht, all_words, spezial_words)
print('------------- Begin Printing, error low on cyan ...')
#dataObject = model_DataOutput.process(dataObject)


print('All done!')