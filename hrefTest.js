function testReplaceEscapeCharacters() {
    const hrefValues = [
        'href="jkfej\\"kf.com"',
        'href="jkfej\\\\"kf.com"',
        'href="jkfej\\\\"',
        'href="jkfej\\"kf.com"',
        'href="jkfej\\"\"kf.com"',
    ];

    hrefValues.forEach((href) => {
        let replacedHref = href.replace(/\\+/g, '');
        console.log('Original:', href);
        console.log('Replaced:', replacedHref);
        console.log('---');
    });
}

testReplaceEscapeCharacters();
