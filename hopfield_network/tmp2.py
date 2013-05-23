# -*- coding: utf-8 -*-
__author__ = 'rkhozinov'

import neurolab as nl
import numpy as np
import pylab as pl

# Создаем обучающую выборку
inp = np.linspace(-7, 7, 20).reshape(20, 1)
tar = np.sin(inp) * 0.5

# Создаем нейронную сеть с одним входом,
# 2я слоями - по 5 и 1 нейрону в каждом
net = nl.net.newff([[-10, 10]], [5, 1])
# Первый аргумент задает диапазоны входных сигналов
# В данном случае сеть имеет один входной сигнал в диапазоне от -10 до 10

# Сменим функцию обучения (по умолчанию nl.train.train_gdx):
net.trainf = nl.train.train_bfgs
#net.trainf = nl.train.train_gdx
# Данная функция обучения использует scipy.optimize.fmin_bfgs
# Поэтому для ее использования необходимо наличие пакета scipy

# Процесс обучения
error = net.train(inp, tar, epochs=500, show=50, goal=0.01)
# inp, tar - обучающие множества
# epochs - число циклов обучения
# goal - цель обучения, значение функционала ошибки при котором обучение будет завершено преждевременно
# show - период вывода информации о состоянии процесса (на данный момент вывод осуществляется в консоль)


# Plot result
pl.subplot(211)
pl.plot(error)
pl.xlabel('Epoch number')
pl.ylabel(u'Error value')

# Испытание сети
inp_test = np.linspace(-8.0, 8.0, 150).reshape(150, 1)
out_test = net.sim(inp_test).flatten()

pl.subplot(212)
pl.plot(inp_test.flat, out_test.flat, '-', inp , tar, 'p')
pl.legend(['train target', 'net output'])
pl.show()
