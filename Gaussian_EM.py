# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:35:21 2016

@author: jgapper
"""

import numpy as np

dat = np.genfromtxt('C:\Users\jgapper\Desktop\CSDS\CS530\Assignment4\iris.csv', delimiter=',')
dat = dat[1:,0:4]

def gaussianEM(data, clusters=3, iteration=5):
    P = np.ones( (clusters,1,4), dtype="float64" )
    P += 1.0 / clusters

    #sample_index = np.array( np.percentile(data, range(100/(clusters+1),100,100/(clusters+1))[:clusters]), dtype="int" ).reshape(clusters,1)
    #sample_index = np.array([[1],[2],[3], [4]])    
    #mu = data[np.zeros((4,1), dtype="int" ), sample_index]
    mu = np.random.rand(clusters, 1, 4)
    print "mu:"
    print mu
    #np.random.seed(100)
    #sample_matrix = np.random.randint( N, size=(clusters, N/4  ) )
    #samples = data[ np.zeros((clusters, N/4), dtype="int"),sample_matrix ]
    #variance = samples.var( axis=1 ).reshape( clusters, 1 )
    #sample_matrix = np.random.randint( N, size=(150,4))
    #samples = np.zeros((3,150, 4), dtype="int")
    samples = np.random.rand(3,150, 4)
    variance = samples.var( axis=1 ).reshape(3,1,4)
    #variance = dat.var( axis=1 ).reshape( clusters, 1 )    

    #E-step
    for i in range( iteration ):
        #squareDistane = ( data - mu ) ** 2
        squareDistane = (np.subtract(dat, mu)**2 )        
        Pxz = 1 / ( np.sqrt( 2 * np.pi ) * np.sqrt(variance)) * np.exp( -squareDistane / ( 2 * variance) ) * Pz
        PzOfx = Pxz / Pxz.sum( axis = 0 )

        #m-step
        sum_P = PzOfx.sum( axis=1 ).reshape( clusters, 1, 4 )
        P = 1. / data.size * sum_P
        mu_new = ( PzOfx * data ).sum( axis = 1 ).reshape(clusters,1, 4) / sum_P
        print ""
        print mu_new
        variance_new = ( ( ( data - mu_new ) ** 2 * PzOfx ).sum( axis = 1 ) ).reshape( clusters, 1, 4) / sum_P
        if( ( np.abs(mu_new - mu) < 1e-6 ).sum() == 2 & ( np.abs( variance_new - variance) < 1e-6 ).sum() == 2 ):
            return Pz, mu_new, variance_new
        else:
            mu = mu_new
            variance = variance_new

    return Pz, mu, variance
"""
mail = np.random.normal( 170, 7, (1, 100) )
femail = np.random.normal( 160, 5, (1, 100) )
child = np.random.normal( 100, 10, (1, 100) )
data = np.c_[mail, femail,child]
np.random.shuffle( data )"""
Pz, u, variance = gaussianEM( dat, clusters=3, iteration=100)