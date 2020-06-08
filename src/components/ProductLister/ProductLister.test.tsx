import React from 'react';
import { render, screen, waitForElement } from '@testing-library/react';
import ProductLister from '.';
// @ts-ignore
import loadJsonData, { setNetworkingResponse } from '../../utils/networking';
jest.mock('../../utils/networking');

const mockData = [
  {
    id: 1,
    name: 'Rustic cottage',
    description: 'Cottage with an awesome view to the mountains',
    image:
      'https://mioapp.s3.amazonaws.com/media/house-rustic-bertrand-bouchez_8SzI3in.jpg',
    product_type: 'House',
  },
  {
    id: 2,
    name: 'Modern house',
    description: 'The best house in town',
    image: 'https://mioapp.s3.amazonaws.com/media/modern-house_7827349.jpg',
    product_type: 'House',
  },
];

describe('ProductLister', () => {
  beforeEach(() => {
    setNetworkingResponse(mockData);
  });

  it('uses mocked networking', async () => {
    render(<ProductLister category="Car" />);
    const sections = await waitForElement(() => screen.getByRole('list'));
    expect(sections).toBeDefined();
    // expect(loadJsonData.mock.calls.length).toBe(1);
    expect(loadJsonData).toHaveBeenCalledTimes(1);
  });

  it('has as many sections as elements in the product data', async () => {
    render(<ProductLister category="house" />);
    const products = await screen.findAllByRole('heading');
    expect(products.length).toBe(2);
  });

  it("has the product's name as title", async () => {
    render(<ProductLister category="house" />);
    const element = await waitForElement(() =>
      screen.findByText(/Rustic cottage/i)
    );
    expect(element).toBeInTheDocument();
  });
});
