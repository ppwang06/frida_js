l.TDEncrypt = function() {
    return function(n) {
        n = JSON.stringify(n);
        n = encodeURIComponent(n);
        var m = "",
        g = 0;
        do {
            var f = n.charCodeAt(g++);
            var d = n.charCodeAt(g++);
            var a = n.charCodeAt(g++);
            var b = f >> 2;
            f = (f & 3) << 4 | d >> 4;
            var e = (d & 15) << 2 | a >> 6;
            var c = a & 63;
            isNaN(d) ? e = c = 64 : isNaN(a) && (c = 64);
            m = m + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(b) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(f) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(e) + "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-".charAt(c)
        } while ( g < n . length );
        return m + "/"
    }
} ();