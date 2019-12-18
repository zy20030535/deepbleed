#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: msharrock
# version: 0.0.1

"""
Registration methods for DeepBleed 

"""

def rigid(fixed, moving):

        '''
        Rigid Registration with ANTS

        Params:
                - moving: ants image, image to move when registering
                - fixed: ants image, template image to register to

        Outputs: 
                - image: registered image
                - transforms: transformation affine matrix
        '''

        kwargs = {'-n': 'BSpline[<order=3>]'}
        tx = ants.registration(fixed, moving, type_of_transform='DenseRigid', mask=None, grad_step=0.1, flow_sigma=3, total_sigma=0, 
                           aff_metric='mattes', aff_sampling=64, syn_metric ='mattes',**kwargs) 
                        
        image = tx['warpedmovout']
        transforms = tx['fwdtransforms']
        return image, transforms


def invert(fixed, moving, transforms):
        '''
        Inverse Transform with ANTS

        Params:
                - image: ants image, image to revert
                - invtransform: affine matrix to use for inverse transform
        Outputs: 
                - image: ants image, inverted
        '''
        kwargs = {'-n': 'BSpline[<order=3>]'}   
        image = ants.apply_transforms(fixed, moving, transformlist = transforms, interpolator = 'nearestNeighbor', whichtoinvert = [True])   

        return image
