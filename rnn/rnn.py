#Python3, Keras, TensorFlow
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils


#вкарваме си данните от сорса.
filename = "sourcebig.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

#преброяване на символите в ресурса и на символите, с които ще работим.
n_chars = len(raw_text)
n_vocab = len(chars)
print("Общо символи: ", n_chars)
print("Общо букви и символи за научаване: ", n_vocab)

# Подготовка на групата от данни

seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print('Общо възможни модели: ', n_patterns)

# първо правим X да бъде [проба, крачка, характеристики]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
# Приравняваме
X = X / float(n_vocab)
# Енкодинг, за да покажем изходната променлива
y = np_utils.to_categorical(dataY)

# Следва да дефинираме LSTM модела с 256 бита памет. Мрежата използва dropout с вероятност 20, а изходния слой използва Dense,
# за да извежда вероятността за предсказване на всичките символи, които сме заредили като ги приравнява между 0 и 1.

# Дефиниране на модела на LSTM
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

filename = "big/weightsbig-improvement-439-1.5411.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')
filepath='big/weightsbig-improvement-{epoch:02d}-{loss:.4f}.hdf5'
checkpoint=ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]


# Следва да зададем 20 епохи на обучение с общо 128 набора от данни.

model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)
