// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: aws/aws_cloud9.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Aws.Cloud9 {

  /// <summary>Holder for reflection information generated from aws/aws_cloud9.proto</summary>
  public static partial class AwsCloud9Reflection {

    #region Descriptor
    /// <summary>File descriptor for aws/aws_cloud9.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static AwsCloud9Reflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChRhd3MvYXdzX2Nsb3VkOS5wcm90bxIWb2FrOS50eXRob24uYXdzLmNsb3Vk",
            "ORoTc2hhcmVkL3NoYXJlZC5wcm90byKDAQoYRW52aXJvbm1lbnRFQzJSZXBv",
            "c2l0b3J5EjcKDXJlc291cmNlX2luZm8YASABKAsyIC5vYWs5LnR5dGhvbi5z",
            "aGFyZWQuUmVzb3VyY2VJbmZvEhYKDnBhdGhfY29tcG9uZW50GAIgASgJEhYK",
            "DnJlcG9zaXRvcnlfdXJsGAMgASgJIpwDCg5FbnZpcm9ubWVudEVDMhI3Cg1y",
            "ZXNvdXJjZV9pbmZvGAEgASgLMiAub2FrOS50eXRob24uc2hhcmVkLlJlc291",
            "cmNlSW5mbxJGCgxyZXBvc2l0b3JpZXMYAiADKAsyMC5vYWs5LnR5dGhvbi5h",
            "d3MuY2xvdWQ5LkVudmlyb25tZW50RUMyUmVwb3NpdG9yeRIRCglvd25lcl9h",
            "cm4YAyABKAkSEwoLZGVzY3JpcHRpb24YBCABKAkSFwoPY29ubmVjdGlvbl90",
            "eXBlGAUgASgJEiMKG2F1dG9tYXRpY19zdG9wX3RpbWVfbWludXRlcxgGIAEo",
            "BRIRCglzdWJuZXRfaWQYByABKAkSFQoNaW5zdGFuY2VfdHlwZRgIIAEoCRI+",
            "CgR0YWdzGAkgAygLMjAub2FrOS50eXRob24uYXdzLmNsb3VkOS5FbnZpcm9u",
            "bWVudEVDMi5UYWdzRW50cnkSDAoEbmFtZRgKIAEoCRorCglUYWdzRW50cnkS",
            "CwoDa2V5GAEgASgJEg0KBXZhbHVlGAIgASgJOgI4ASJKCgZDbG91ZDkSQAoQ",
            "ZW52aXJvbm1lbnRfZV9jMhgBIAMoCzImLm9hazkudHl0aG9uLmF3cy5jbG91",
            "ZDkuRW52aXJvbm1lbnRFQzJiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository), global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository.Parser, new[]{ "ResourceInfo", "PathComponent", "RepositoryUrl" }, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2), global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2.Parser, new[]{ "ResourceInfo", "Repositories", "OwnerArn", "Description", "ConnectionType", "AutomaticStopTimeMinutes", "SubnetId", "InstanceType", "Tags", "Name" }, null, null, null, new pbr::GeneratedClrTypeInfo[] { null, }),
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Aws.Cloud9.Cloud9), global::Oak9.Tython.Aws.Cloud9.Cloud9.Parser, new[]{ "EnvironmentEC2" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class EnvironmentEC2Repository : pb::IMessage<EnvironmentEC2Repository>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<EnvironmentEC2Repository> _parser = new pb::MessageParser<EnvironmentEC2Repository>(() => new EnvironmentEC2Repository());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<EnvironmentEC2Repository> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Cloud9.AwsCloud9Reflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2Repository() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2Repository(EnvironmentEC2Repository other) : this() {
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      pathComponent_ = other.pathComponent_;
      repositoryUrl_ = other.repositoryUrl_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2Repository Clone() {
      return new EnvironmentEC2Repository(this);
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 1;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    /// <summary>Field number for the "path_component" field.</summary>
    public const int PathComponentFieldNumber = 2;
    private string pathComponent_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string PathComponent {
      get { return pathComponent_; }
      set {
        pathComponent_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "repository_url" field.</summary>
    public const int RepositoryUrlFieldNumber = 3;
    private string repositoryUrl_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string RepositoryUrl {
      get { return repositoryUrl_; }
      set {
        repositoryUrl_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as EnvironmentEC2Repository);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(EnvironmentEC2Repository other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      if (PathComponent != other.PathComponent) return false;
      if (RepositoryUrl != other.RepositoryUrl) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      if (PathComponent.Length != 0) hash ^= PathComponent.GetHashCode();
      if (RepositoryUrl.Length != 0) hash ^= RepositoryUrl.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      if (PathComponent.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(PathComponent);
      }
      if (RepositoryUrl.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(RepositoryUrl);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      if (PathComponent.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(PathComponent);
      }
      if (RepositoryUrl.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(RepositoryUrl);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      if (PathComponent.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(PathComponent);
      }
      if (RepositoryUrl.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(RepositoryUrl);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(EnvironmentEC2Repository other) {
      if (other == null) {
        return;
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      if (other.PathComponent.Length != 0) {
        PathComponent = other.PathComponent;
      }
      if (other.RepositoryUrl.Length != 0) {
        RepositoryUrl = other.RepositoryUrl;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            PathComponent = input.ReadString();
            break;
          }
          case 26: {
            RepositoryUrl = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            PathComponent = input.ReadString();
            break;
          }
          case 26: {
            RepositoryUrl = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class EnvironmentEC2 : pb::IMessage<EnvironmentEC2>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<EnvironmentEC2> _parser = new pb::MessageParser<EnvironmentEC2>(() => new EnvironmentEC2());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<EnvironmentEC2> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Cloud9.AwsCloud9Reflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2(EnvironmentEC2 other) : this() {
      resourceInfo_ = other.resourceInfo_ != null ? other.resourceInfo_.Clone() : null;
      repositories_ = other.repositories_.Clone();
      ownerArn_ = other.ownerArn_;
      description_ = other.description_;
      connectionType_ = other.connectionType_;
      automaticStopTimeMinutes_ = other.automaticStopTimeMinutes_;
      subnetId_ = other.subnetId_;
      instanceType_ = other.instanceType_;
      tags_ = other.tags_.Clone();
      name_ = other.name_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public EnvironmentEC2 Clone() {
      return new EnvironmentEC2(this);
    }

    /// <summary>Field number for the "resource_info" field.</summary>
    public const int ResourceInfoFieldNumber = 1;
    private global::Oak9.Tython.Shared.ResourceInfo resourceInfo_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Shared.ResourceInfo ResourceInfo {
      get { return resourceInfo_; }
      set {
        resourceInfo_ = value;
      }
    }

    /// <summary>Field number for the "repositories" field.</summary>
    public const int RepositoriesFieldNumber = 2;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository> _repeated_repositories_codec
        = pb::FieldCodec.ForMessage(18, global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository> repositories_ = new pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2Repository> Repositories {
      get { return repositories_; }
    }

    /// <summary>Field number for the "owner_arn" field.</summary>
    public const int OwnerArnFieldNumber = 3;
    private string ownerArn_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string OwnerArn {
      get { return ownerArn_; }
      set {
        ownerArn_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "description" field.</summary>
    public const int DescriptionFieldNumber = 4;
    private string description_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Description {
      get { return description_; }
      set {
        description_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "connection_type" field.</summary>
    public const int ConnectionTypeFieldNumber = 5;
    private string connectionType_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string ConnectionType {
      get { return connectionType_; }
      set {
        connectionType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "automatic_stop_time_minutes" field.</summary>
    public const int AutomaticStopTimeMinutesFieldNumber = 6;
    private int automaticStopTimeMinutes_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int AutomaticStopTimeMinutes {
      get { return automaticStopTimeMinutes_; }
      set {
        automaticStopTimeMinutes_ = value;
      }
    }

    /// <summary>Field number for the "subnet_id" field.</summary>
    public const int SubnetIdFieldNumber = 7;
    private string subnetId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string SubnetId {
      get { return subnetId_; }
      set {
        subnetId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "instance_type" field.</summary>
    public const int InstanceTypeFieldNumber = 8;
    private string instanceType_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string InstanceType {
      get { return instanceType_; }
      set {
        instanceType_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "tags" field.</summary>
    public const int TagsFieldNumber = 9;
    private static readonly pbc::MapField<string, string>.Codec _map_tags_codec
        = new pbc::MapField<string, string>.Codec(pb::FieldCodec.ForString(10, ""), pb::FieldCodec.ForString(18, ""), 74);
    private readonly pbc::MapField<string, string> tags_ = new pbc::MapField<string, string>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::MapField<string, string> Tags {
      get { return tags_; }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 10;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as EnvironmentEC2);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(EnvironmentEC2 other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ResourceInfo, other.ResourceInfo)) return false;
      if(!repositories_.Equals(other.repositories_)) return false;
      if (OwnerArn != other.OwnerArn) return false;
      if (Description != other.Description) return false;
      if (ConnectionType != other.ConnectionType) return false;
      if (AutomaticStopTimeMinutes != other.AutomaticStopTimeMinutes) return false;
      if (SubnetId != other.SubnetId) return false;
      if (InstanceType != other.InstanceType) return false;
      if (!Tags.Equals(other.Tags)) return false;
      if (Name != other.Name) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (resourceInfo_ != null) hash ^= ResourceInfo.GetHashCode();
      hash ^= repositories_.GetHashCode();
      if (OwnerArn.Length != 0) hash ^= OwnerArn.GetHashCode();
      if (Description.Length != 0) hash ^= Description.GetHashCode();
      if (ConnectionType.Length != 0) hash ^= ConnectionType.GetHashCode();
      if (AutomaticStopTimeMinutes != 0) hash ^= AutomaticStopTimeMinutes.GetHashCode();
      if (SubnetId.Length != 0) hash ^= SubnetId.GetHashCode();
      if (InstanceType.Length != 0) hash ^= InstanceType.GetHashCode();
      hash ^= Tags.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      repositories_.WriteTo(output, _repeated_repositories_codec);
      if (OwnerArn.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(OwnerArn);
      }
      if (Description.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Description);
      }
      if (ConnectionType.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ConnectionType);
      }
      if (AutomaticStopTimeMinutes != 0) {
        output.WriteRawTag(48);
        output.WriteInt32(AutomaticStopTimeMinutes);
      }
      if (SubnetId.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(SubnetId);
      }
      if (InstanceType.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(InstanceType);
      }
      tags_.WriteTo(output, _map_tags_codec);
      if (Name.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (resourceInfo_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ResourceInfo);
      }
      repositories_.WriteTo(ref output, _repeated_repositories_codec);
      if (OwnerArn.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(OwnerArn);
      }
      if (Description.Length != 0) {
        output.WriteRawTag(34);
        output.WriteString(Description);
      }
      if (ConnectionType.Length != 0) {
        output.WriteRawTag(42);
        output.WriteString(ConnectionType);
      }
      if (AutomaticStopTimeMinutes != 0) {
        output.WriteRawTag(48);
        output.WriteInt32(AutomaticStopTimeMinutes);
      }
      if (SubnetId.Length != 0) {
        output.WriteRawTag(58);
        output.WriteString(SubnetId);
      }
      if (InstanceType.Length != 0) {
        output.WriteRawTag(66);
        output.WriteString(InstanceType);
      }
      tags_.WriteTo(ref output, _map_tags_codec);
      if (Name.Length != 0) {
        output.WriteRawTag(82);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (resourceInfo_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ResourceInfo);
      }
      size += repositories_.CalculateSize(_repeated_repositories_codec);
      if (OwnerArn.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(OwnerArn);
      }
      if (Description.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Description);
      }
      if (ConnectionType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(ConnectionType);
      }
      if (AutomaticStopTimeMinutes != 0) {
        size += 1 + pb::CodedOutputStream.ComputeInt32Size(AutomaticStopTimeMinutes);
      }
      if (SubnetId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(SubnetId);
      }
      if (InstanceType.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(InstanceType);
      }
      size += tags_.CalculateSize(_map_tags_codec);
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(EnvironmentEC2 other) {
      if (other == null) {
        return;
      }
      if (other.resourceInfo_ != null) {
        if (resourceInfo_ == null) {
          ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
        }
        ResourceInfo.MergeFrom(other.ResourceInfo);
      }
      repositories_.Add(other.repositories_);
      if (other.OwnerArn.Length != 0) {
        OwnerArn = other.OwnerArn;
      }
      if (other.Description.Length != 0) {
        Description = other.Description;
      }
      if (other.ConnectionType.Length != 0) {
        ConnectionType = other.ConnectionType;
      }
      if (other.AutomaticStopTimeMinutes != 0) {
        AutomaticStopTimeMinutes = other.AutomaticStopTimeMinutes;
      }
      if (other.SubnetId.Length != 0) {
        SubnetId = other.SubnetId;
      }
      if (other.InstanceType.Length != 0) {
        InstanceType = other.InstanceType;
      }
      tags_.MergeFrom(other.tags_);
      if (other.Name.Length != 0) {
        Name = other.Name;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            repositories_.AddEntriesFrom(input, _repeated_repositories_codec);
            break;
          }
          case 26: {
            OwnerArn = input.ReadString();
            break;
          }
          case 34: {
            Description = input.ReadString();
            break;
          }
          case 42: {
            ConnectionType = input.ReadString();
            break;
          }
          case 48: {
            AutomaticStopTimeMinutes = input.ReadInt32();
            break;
          }
          case 58: {
            SubnetId = input.ReadString();
            break;
          }
          case 66: {
            InstanceType = input.ReadString();
            break;
          }
          case 74: {
            tags_.AddEntriesFrom(input, _map_tags_codec);
            break;
          }
          case 82: {
            Name = input.ReadString();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (resourceInfo_ == null) {
              ResourceInfo = new global::Oak9.Tython.Shared.ResourceInfo();
            }
            input.ReadMessage(ResourceInfo);
            break;
          }
          case 18: {
            repositories_.AddEntriesFrom(ref input, _repeated_repositories_codec);
            break;
          }
          case 26: {
            OwnerArn = input.ReadString();
            break;
          }
          case 34: {
            Description = input.ReadString();
            break;
          }
          case 42: {
            ConnectionType = input.ReadString();
            break;
          }
          case 48: {
            AutomaticStopTimeMinutes = input.ReadInt32();
            break;
          }
          case 58: {
            SubnetId = input.ReadString();
            break;
          }
          case 66: {
            InstanceType = input.ReadString();
            break;
          }
          case 74: {
            tags_.AddEntriesFrom(ref input, _map_tags_codec);
            break;
          }
          case 82: {
            Name = input.ReadString();
            break;
          }
        }
      }
    }
    #endif

  }

  public sealed partial class Cloud9 : pb::IMessage<Cloud9>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Cloud9> _parser = new pb::MessageParser<Cloud9>(() => new Cloud9());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<Cloud9> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Aws.Cloud9.AwsCloud9Reflection.Descriptor.MessageTypes[2]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Cloud9() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Cloud9(Cloud9 other) : this() {
      environmentEC2_ = other.environmentEC2_.Clone();
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Cloud9 Clone() {
      return new Cloud9(this);
    }

    /// <summary>Field number for the "environment_e_c2" field.</summary>
    public const int EnvironmentEC2FieldNumber = 1;
    private static readonly pb::FieldCodec<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2> _repeated_environmentEC2_codec
        = pb::FieldCodec.ForMessage(10, global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2.Parser);
    private readonly pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2> environmentEC2_ = new pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2>();
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public pbc::RepeatedField<global::Oak9.Tython.Aws.Cloud9.EnvironmentEC2> EnvironmentEC2 {
      get { return environmentEC2_; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as Cloud9);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(Cloud9 other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if(!environmentEC2_.Equals(other.environmentEC2_)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      hash ^= environmentEC2_.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      environmentEC2_.WriteTo(output, _repeated_environmentEC2_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      environmentEC2_.WriteTo(ref output, _repeated_environmentEC2_codec);
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      size += environmentEC2_.CalculateSize(_repeated_environmentEC2_codec);
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(Cloud9 other) {
      if (other == null) {
        return;
      }
      environmentEC2_.Add(other.environmentEC2_);
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            environmentEC2_.AddEntriesFrom(input, _repeated_environmentEC2_codec);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            environmentEC2_.AddEntriesFrom(ref input, _repeated_environmentEC2_codec);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
