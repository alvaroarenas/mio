let _response = { data: 'foo' };

const loadJsonDataMock = async (url: string) => {
  const returnValue = await Promise.resolve(_response);

  return returnValue;
};

const loadJsonData = jest.fn(loadJsonDataMock);

export const setNetworkingResponse = (response: any) => (_response = response);

export default loadJsonData;
