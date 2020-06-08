import { enableFetchMocks } from 'jest-fetch-mock';
import loadJsonData from './networking';
import fetchMock from 'jest-fetch-mock';
enableFetchMocks();

describe('networking', () => {
  beforeEach(() => {
    fetchMock.resetMocks();
  });

  it('calls the correct url', async () => {
    fetchMock.mockResponseOnce(JSON.stringify({ data: '12345' }));
    const url = 'https://mio-app.herkokuapp.com/api/product/';

    const response = await loadJsonData(url);

    expect(fetchMock).toHaveBeenCalledWith(url);
    expect(response.data).toEqual('12345');
  });
});
