import { Injectable } from '@nestjs/common';
import { join } from 'path';
import * as tf from '@tensorflow/tfjs';

@Injectable()
export class AppService {
  async getModel(): Promise<tf.LayersModel> {
    const filePath = join('file://', __dirname, './src/models/2x1.json');
    console.log(filePath);
    const model = await tf.loadLayersModel(filePath);
    return model;
  }
}
