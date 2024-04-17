import { Injectable } from '@nestjs/common';
import * as tf from '@tensorflow/tfjs';

@Injectable()
export class AppService {
  async getModel(): Promise<tf.LayersModel> {
    const model = await tf.loadLayersModel(
      'https://raw.githubusercontent.com/ikemtz/ceis312/master/WebServerExample/tensor-flow-2x1/src/models/2x1.json');
    return model;
  }
}
