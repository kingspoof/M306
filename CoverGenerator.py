from Modules.DataInput import DataInput
from Modules.DataProcessing import DataProcessing
from Modules.DataOutput import DataOutput


model_DataInput = DataInput()
model_DataProcessing = DataProcessing()
model_DataOutput = DataOutput()


print('------------- Begin reading ...')
height, widht, all_words, spezial_words, paragraph = model_DataInput.process()
print('------------- Begin Processing ...')
field_words, field_words_caps, field = model_DataProcessing.process(height, widht, all_words, spezial_words, paragraph)
print('------------- Begin Printing, error low on cyan ...')
model_DataOutput.process(field_words, field_words_caps, field)


print('All done!')