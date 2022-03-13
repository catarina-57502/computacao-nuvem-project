import { describe, expect, test } from '@jest/globals';
import SwaggerUI from '../.';

describe('webpack browser es-bundle-core build', () => {
  test('should export a function for es-bundle-core', () => {
    expect(SwaggerUI).toBeInstanceOf(Function);
  });
});
