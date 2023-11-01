var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.ImgThumbnail = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData(props.value);
    }

    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
            },
        },
        React.createElement(
            'img',
            {
                onClick: onClick,
                style: {width: '100%', height: 'auto'},
                src: props.value,
            },
        )
    );
};
