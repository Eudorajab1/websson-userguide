Environments
============

By default once you have successfully activated your :doc:`subscription <subscriptions>` you are ready to create an environment
or even multiple environments based on your subscription features.

Typically your subscripion will consist of the following features per environment:-

        *  Disk space
        *  Ram
        *  Database engines
        *  Database admin/GUI
        *  IDE / editors
        *  Domain names
        *  Instances

If your subscription offers multiple environments, the above are cumulative across all environments and with a few exceptions
your total allowable value for any feature will be the product of the number of environmnets and the feature value.

In essence this means that one environment may exceed the feature value but the total across all environmnets should not exceed the 
cumulative total.

.. note::

    For the purpose of this document we will assume a typical setup consisting of two environments. One will be for development
    while the other will be for deployment.

.. _new:

Creating a new environment
--------------------------

Creating a new enviroment / environments is achieved by either clicking the **Environments** button on your **Portal Landing Page**
or secting the **Environments** option from your menu.

This will take you to the **Envirornment Manager** where a list of your existing environments are displayed along with 
options presented in the form of links / action buttons.

To create a new environment simply select the **New Environment** option and you will be propmted to enter information
relating to the type of envrionment that you wish to create.

Irrestpective of the type of environment you are creating the following minimal information is required in order to 
create an environment:-

    *  Cap Instance - the pyhsical location and type of environment (Typically production or development)
    *  Environment Type - the base framework (django, streamilt, jupyter etc)
    *  Name - A unique name that cannot include non alphanumeric characters

Additional information such as Admin User, Admin Password and Admin URL will optionally be required based on the type of
environment you are creating.

Once all the information has been entered the environment is automatically created based on subscription features.

.. _customising:

Customising
-----------

Customising an environmnet is also done via the **Environment Manager** option from the menu then by selecting 
the **Admin** action button from the environment you wissh to customise.

You will be presented with all the options that are customisable based on your selected subscription and simply following
the procedure for customising any and all features required.

.. _removing:

Removing
--------

In the event that you no longer need an environment you can simply remove the environment by selecting the **Deete** action
button on the relevant environment.

This will pormpt you to confirm you wish to delete the environment and by accepting the environment will be removed.

.. note::

    All data for the deleted environment will be available for a period of 30 (thirty) days after the environment
    is deleted but we strongly reccomend that you manke backups or download any data you wish to keep before
    removing an active environment.
    

