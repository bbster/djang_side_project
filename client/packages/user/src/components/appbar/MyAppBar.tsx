import React from 'react';
import Img from 'next/image';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import logo from './Logo.png';
import reactLogo from './react-logo.png';

import { useCartPloc } from 'pages/index';
import { usePlocState } from 'modules/common/usePlocState';

const useStyles = makeStyles(() => ({
    toolbar: {
        justifyContent: 'space-between',
        maxWidth: '800',
    },
}));

const MyAppBar: React.FC = () => {
    const classes = useStyles();
    const ploc = useCartPloc();
    const state = usePlocState(ploc);

    const totalItems = state.kind === 'UpdatedCartState' ? state.totalItems : 0;

    return (
        <AppBar position="static">
            <Toolbar className={classes.toolbar}>
                <div>
                    <Img src={logo} width={150} height={32} alt="logo" />
                    <Img src={reactLogo} width={40} height={32} alt="react logo" />
                </div>

                <IconButton color="inherit">
                    <Badge badgeContent={totalItems} color="secondary">
                        <ShoppingCartIcon onClick={() => ploc.openCart()} />
                    </Badge>
                </IconButton>
            </Toolbar>
        </AppBar>
    );
};

export default MyAppBar;
