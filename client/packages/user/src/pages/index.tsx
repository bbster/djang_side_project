import React from 'react';

import MyAppBar from 'components/appbar/MyAppBar';

import { CartPloc, dependenciesLocator } from '@side-client/core';

import { createContext } from 'modules/common/Context';
import ProductList from 'modules/products/ProductList';
import CartDrawer from 'modules/cart/CartDrawer';

// import { GetServerSidePropsContext } from "next";
// import Head from "next/head";
const [blocContext, usePloc] = createContext<CartPloc>();

export const useCartPloc = usePloc;

export async function getServerSideProps() {
    return { props: {} };
}

function Index() {
    return (
        <blocContext.Provider value={dependenciesLocator.provideCartPloc()}>
            <MyAppBar />
            <ProductList />
            <CartDrawer />
        </blocContext.Provider>
    );
}

export default Index;
