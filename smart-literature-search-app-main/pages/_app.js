import '../styles/globals.css';
import { Provider } from 'react-redux';
import { createWrapper } from 'next-redux-wrapper';
import store from '../src/redux/store';
import { GoogleOAuthProvider } from '@react-oauth/google';
const MyApp = ({ Component, pageProps }) => {
    return (
        <Provider store={store}>
            <GoogleOAuthProvider clientId={process.env.NEXT_PUBLIC_CLIENTID}>
                <Component {...pageProps} />
            </GoogleOAuthProvider>
        </Provider>
    );
};

const makeStore = () => store;
const wrapper = createWrapper(makeStore);

export default wrapper.withRedux(MyApp);
