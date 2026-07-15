<?php
// Simple router for linzihyang studio website
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$uri = rtrim($uri, '/');

// Map routes to template files
$routes = [
    '/' => 'home.html',
    '/about' => 'about.html',
    '/portfolio' => 'portfolio.html',
    '/courses' => 'courses.html',
    '/contact' => 'contact.html'
];

// Handle routes
if (isset($routes[$uri])) {
    $template_file = __DIR__ . '/templates/' . $routes[$uri];
    if (file_exists($template_file)) {
        // Load and render the template
        include $template_file;
        exit;
    }
}

// Handle static files
if (file_exists(__DIR__ . $uri)) {
    $info = pathinfo($uri);
    $ext = strtolower($info['extension'] ?? '');
    $mime_types = [
        'css' => 'text/css',
        'js' => 'application/javascript',
        'jpg' => 'image/jpeg',
        'jpeg' => 'image/jpeg',
        'png' => 'image/png',
        'gif' => 'image/gif',
        'svg' => 'image/svg+xml',
        'ico' => 'image/x-icon'
    ];
    
    if (isset($mime_types[$ext])) {
        header('Content-Type: ' . $mime_types[$ext]);
    }
    include __DIR__ . $uri;
    exit;
}

// Default to index.html if exists
if (file_exists(__DIR__ . '/index.html')) {
    include __DIR__ . '/index.html';
    exit;
}

http_response_code(404);
echo '404 Not Found';
?>
