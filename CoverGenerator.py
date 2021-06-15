from Modules.DataInput import DataInput
from Modules.DataProcessing import DataProcessing
from Modules.DataOutput import DataOutput

from Datamodels.DataObject import DataObject


model_DataInput = DataInput()
model_DataProcessing = DataProcessing()
model_DataOutput = DataOutput()


dataObject = DataObject()


dataObject.height, dataObject.width, dataObject.all_words, dataObject.spezial_words = model_DataInput.process()
#dataObject = model_DataProcessing.process(dataObject)
#dataObject = model_DataOutput.process(dataObject)


print('All done!')