module.exports = {
    async headers() {
        return [
            {
                source: "/(.*)",
                headers: [
                    {
                        key: "Content-Security-Policy",
                        value:
                            "script-src 'self' https://apis.google.com https://www.gstatic.com https://accounts.google.com/gsi/client; frame-src 'self' https://accounts.google.com;",
                    },
                    {
                        key: "Cross-Origin-Opener-Policy",
                        value: "same-origin-allow-popups",
                    },
                ],
            },
        ];
    },
};