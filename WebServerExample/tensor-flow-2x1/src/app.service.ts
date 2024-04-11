import { Injectable } from '@nestjs/common';
import * as tf from '@tensorflow/tfjs';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}
