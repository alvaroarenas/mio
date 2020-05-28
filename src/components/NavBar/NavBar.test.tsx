import React from 'react';
import { render, screen } from '@testing-library/react';
// import NavBar from './NavBar';
import NavBar from './NavBar';
import 'jest-styled-components';

test('renders without crashing', () => {
  const title = 'Mio';
  render(<NavBar title={title} />);
  screen.getByRole('heading', { name: /mio/i });
});

test('renders the giving title', () => {
  const title = 'This is a new longer title';
  render(<NavBar title={title} />);
  screen.getByRole('heading', { name: /This is a new longer title/ });
});

it('matches the snapshot', () => {
  const { container } = render(<NavBar title={'The title'} />);
  expect(container.firstChild).toMatchSnapshot();
});
