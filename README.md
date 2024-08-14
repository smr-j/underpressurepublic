# Under Pressure : Mapping Barometric Variation
A repository for CS6620: Cloud Computing's Final Project.

## Background

While sparse research exists on the topic, large variations in barometric pressure can affect how humans experience pain.
When barometric pressure drops, as it usually does prior to bad weather, it can:
* lead to tissue expansion which puts pressure on joints and worsens arthritis
* lead to pressure differentials between the outside and the inside of the body, which can worsen headaches, especially migraines and headaches caused by sinusitis
However, most studies find insignificant results when data is pooled; barometric pressure has more influence at the individual level.

## Project Progress

There are two different repositories for this project, marking two different approaches and consolidating all the littler tasks that I had set for myself. 

The other repository is the ancestor to this one, and it uses localstack, boto3, docker, and python to create an S3 bucket that would collect information for each location pulled from the weather.gov APIs as well as store the static website that displays the output map. However, at this stage in time, this project simply creates the S3 bucket and then carries out the remaining tasks in the current workflow, namely, creating a static website that displays a map with points that are color-coordinated based on the amount of pressure variation and also display some other information when clicked on. 

The other repository is this one, which replaces boto3 with Terraform and thus uses Terraform to create an S3 bucket that, in an ideal situation, would an object for each location that is a point on the map. The object stores information for each location pulled from the weather.gov APIs. Given that everything is Dockerized, I did not need to use S3 to store the website. This is in some ways simpler than its predecessor, mostly because I was focused on ensuring that Terraform was integrated with everything else.


## Challenges

I found a lot of different things to be challenging. 

One of the bigger challenges I faced was with the NWS APIs, which were not well-organized with regards to telling me what information I would be able to pull. I thought I had found an API call that would provide me with barometric pressure, which isn't a common weather metric, but in practice, the barometric pressure field was empty when I applied it to my intended locations in Maine. This led to me populating the current iteration of my project with 'fake' data to create a mockup.

I also struggled quite a bit with setting up the architecture for this project, although part of that is because the workflows changed as I worked on the project to become more practical or become better-suited to the production environment. 

## Architecture Diagrams

### Version 1

<img src="figs/workflow_v1.png" alt="The first iteration of the architecture diagram" style="width: 600px;">

### Version 2

<img src="figs/workflow_v2.png" alt="The second iteration of the architecture diagram" style="width: 600px;">

### Version 3

<img src="figs/workflow_v3.png" alt="Progress towards a more realistic architecture diagram." style="width: 600px;">


## Next Steps

## Acknowledgments

A huge thanks to Jim Sheldon for all of his help putting together this project.

## Sources & Consulted Sites

https://barometricpressure.app/content/understanding-high-low-pressure-readings
https://forecast.weather.gov/glossary.php?word=PRES
https://stackoverflow.com/questions/70407525/terraform-gives-errors-failed-to-load-plugin-schemas
https://docs.localstack.cloud/tutorials/s3-static-website-terraform/
https://docs.localstack.cloud/user-guide/integrations/terraform/
