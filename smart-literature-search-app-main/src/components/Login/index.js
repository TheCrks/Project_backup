import { useRouter } from 'next/router';
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';
import LocalStorage from '../../utils/localStorage.utils';
import { jwtDecode } from "jwt-decode";

const clientId = process.env.NEXT_PUBLIC_CLIENTID;

const LoginComponent = () => {
    const router = useRouter();

    const onSuccess = (res) => {
        try {
            const decodedToken = jwtDecode(res.credential); // Decode the token

            LocalStorage.setItemWithExpiry('user', decodedToken, 60);
            router.push('/');
        } catch (error) {
        }
    };

    const onFailure = (res) => {
        console.log('[Login Failed] res:', res);
    };

    return (
        <GoogleOAuthProvider clientId={clientId}>
            <div className='h-screen flex bg-gray-bg1'>
                <div className='w-full max-w-md m-auto bg-white rounded-lg border border-primaryBorder shadow-default py-10 px-16'>
                    <h1 className='text-2xl font-medium text-primary mt-4 mb-12 text-center'>
                        Log in to your account 🔐
                    </h1>

                    <div className='flex justify-center items-center mt-6'>
                        <GoogleLogin
                            onSuccess={onSuccess}
                            onFailure={onFailure}
                            cookiePolicy={'single_host_origin'}
                            isSignedIn={true}
                            className=''
                        />
                    </div>
                </div>
            </div>
        </GoogleOAuthProvider>
    );
};

export default LoginComponent;
