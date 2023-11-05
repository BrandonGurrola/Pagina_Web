<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInitfe1bc60b19068fd5d4cb6b9a927d8266
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    /**
     * @return \Composer\Autoload\ClassLoader
     */
    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        require __DIR__ . '/platform_check.php';

        spl_autoload_register(array('ComposerAutoloaderInitfe1bc60b19068fd5d4cb6b9a927d8266', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader(\dirname(__DIR__));
        spl_autoload_unregister(array('ComposerAutoloaderInitfe1bc60b19068fd5d4cb6b9a927d8266', 'loadClassLoader'));

        require __DIR__ . '/autoload_static.php';
        call_user_func(\Composer\Autoload\ComposerStaticInitfe1bc60b19068fd5d4cb6b9a927d8266::getInitializer($loader));

        $loader->register(true);

        return $loader;
    }
}
